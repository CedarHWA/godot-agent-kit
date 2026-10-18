[CmdletBinding()]
param([string]$Python, [string]$Godot)
$ErrorActionPreference = 'Stop'
$repository = Split-Path -Parent $PSScriptRoot
if (-not $Python) { $Python = Join-Path $repository '.venv\Scripts\python.exe' }
Push-Location $repository
try {
    & $Python -B toolkit/validate.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    & $Python -B tests/run.py
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    if ($Godot) {
        & $Python -B tests/integration.py --godot $Godot
        if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    }
} finally {
    Pop-Location
}
