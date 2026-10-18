[CmdletBinding()]
param(
    [ValidateSet('codex','deepseek-harness','both')][string]$Agent = 'both',
    [ValidateSet('core','desktop-wai','endpoint')][string]$Profile = 'core',
    [string]$Project,
    [string]$Config,
    [string]$Python = 'python',
    [string]$Report,
    [switch]$VerifyModel
)
$ErrorActionPreference = 'Stop'
$kitArgs = @('-B', (Join-Path $PSScriptRoot 'toolkit\cli.py'), 'doctor', '--agent', $Agent, '--profile', $Profile)
if ($Project) { $kitArgs += @('--project', $Project) }
if ($Config) { $kitArgs += @('--config', $Config) }
if ($Report) { $kitArgs += @('--report', $Report) }
if ($VerifyModel) { $kitArgs += '--verify-model' }
& $Python @kitArgs
exit $LASTEXITCODE
