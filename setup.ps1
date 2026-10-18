[CmdletBinding()]
param([string]$Python = 'python', [switch]$Comfy)
$ErrorActionPreference = 'Stop'
$environmentDir = Join-Path $PSScriptRoot $(if ($Comfy) { '.local\comfy-runtime' } else { '.venv' })
$requirements = Join-Path $PSScriptRoot $(if ($Comfy) { 'requirements-comfy.txt' } else { 'requirements.txt' })
$environmentPython = Join-Path $environmentDir 'Scripts\python.exe'
if (-not (Test-Path -LiteralPath $environmentPython)) {
    & $Python -m venv $environmentDir
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
& $environmentPython -m pip install --disable-pip-version-check -r $requirements
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Output "Environment ready: $environmentPython"
Write-Output 'No global Python environment, Godot installation, models, or agent settings were changed.'
