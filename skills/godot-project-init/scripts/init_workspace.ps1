param(
    [Parameter(Mandatory = $true)][ValidateSet('begin', 'clean')][string]$Action,
    [Parameter(Mandatory = $true)][string]$Project,
    [string]$RunDir
)
$ErrorActionPreference = 'Stop'

function Get-CheckedPath([string]$Value) {
    $absolute = [IO.Path]::GetFullPath($Value).TrimEnd('\', '/')
    $ancestor = $absolute
    while ($ancestor) {
        if (Test-Path -LiteralPath $ancestor) {
            $item = Get-Item -LiteralPath $ancestor -Force
            if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
                throw "Refusing a reparse point in path: $ancestor"
            }
        }
        $ancestor = Split-Path -Parent $ancestor
    }
    return $absolute
}

$projectPath = Get-CheckedPath $Project
$driveRoot = [IO.Path]::GetPathRoot($projectPath).TrimEnd('\', '/')
if ($projectPath -eq $driveRoot -or (Split-Path -Parent $projectPath).TrimEnd('\', '/') -eq $driveRoot) {
    throw 'Choose a project below an existing parent folder, not a drive root.'
}
$existingParent = $projectPath
while (-not (Test-Path -LiteralPath $existingParent)) {
    $existingParent = Split-Path -Parent $existingParent
}
if ($existingParent.TrimEnd('\', '/') -eq $driveRoot) {
    throw 'This would create a folder in the drive root.'
}
$workPath = Get-CheckedPath (Join-Path $projectPath 'work')

if ($Action -eq 'begin') {
    $runPath = Join-Path $workPath ('init-' + [guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Path $runPath -Force | Out-Null
    $marker = [ordered]@{ schema = 1; purpose = 'godot-project-init'; project = $projectPath; run_dir = $runPath }
    $json = $marker | ConvertTo-Json
    [IO.File]::WriteAllText((Join-Path $runPath '.init-owner.json'), $json, [Text.UTF8Encoding]::new($false))
    $marker | ConvertTo-Json -Compress
    exit 0
}

if (-not $RunDir) { throw 'clean requires -RunDir returned by begin.' }
$runPath = Get-CheckedPath $RunDir
if ((Split-Path -Parent $runPath) -ne $workPath -or (Split-Path -Leaf $runPath) -notmatch '^init-[0-9a-f]{32}$') {
    throw 'Only a single owned init run directly inside project/work can be cleaned.'
}
if (-not (Test-Path -LiteralPath $runPath)) {
    @{ removed = $false; reason = 'already_absent'; run_dir = $runPath } | ConvertTo-Json -Compress
    exit 0
}
$markerPath = Get-CheckedPath (Join-Path $runPath '.init-owner.json')
$marker = Get-Content -LiteralPath $markerPath -Raw -Encoding UTF8 | ConvertFrom-Json
if ($marker.schema -ne 1 -or $marker.purpose -ne 'godot-project-init' -or $marker.project -ne $projectPath -or $marker.run_dir -ne $runPath) {
    throw 'Run ownership marker does not match this project and directory.'
}

# Check each entry before descending; never follow a junction during cleanup.
$pending = [Collections.Generic.Stack[string]]::new()
$pending.Push($runPath)
$fileCount = 0
while ($pending.Count -gt 0) {
    $directory = $pending.Pop()
    foreach ($item in (Get-ChildItem -LiteralPath $directory -Force)) {
        if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) {
            throw "Refusing cleanup through a reparse point: $($item.FullName)"
        }
        if ($item.PSIsContainer) { $pending.Push($item.FullName) } else { $fileCount++ }
    }
}
Remove-Item -LiteralPath $runPath -Recurse -Force
@{ removed = $true; run_dir = $runPath; files_removed = $fileCount } | ConvertTo-Json -Compress
