[CmdletBinding()]
param([string]$Godot, [string]$Python, [switch]$SkipLint, [switch]$IsolateEditor, [string]$ReportDir, [string[]]$TestScript)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$settingsPath = Join-Path $projectRoot '.local\toolchain.json'
if (-not $Python -and (Test-Path -LiteralPath $settingsPath)) {
    $settings = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json
    $Python = $settings.python
}
if (-not $Python) { $Python = 'python' }
$checkArgs = @((Join-Path $PSScriptRoot 'check_project.py'))
if ($Godot) { $checkArgs += @('--godot', $Godot) }
if ($SkipLint) { $checkArgs += '--skip-lint' }
if ($IsolateEditor) { $checkArgs += '--isolate-editor' }
if ($ReportDir) { $checkArgs += @('--report-dir', $ReportDir) }
foreach ($scriptPath in $TestScript) { $checkArgs += @('--test-script', $scriptPath) }
& $Python @checkArgs
exit $LASTEXITCODE
