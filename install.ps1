[CmdletBinding()]
param(
    [ValidateSet('codex','deepseek-harness','both')][string]$Agent = 'codex',
    [ValidateSet('project','user')][string]$Scope = 'project',
    [string]$Project,
    [ValidateSet('both','init','dev')][string]$Skills = 'both',
    [ValidateSet('install','uninstall','rollback','recover')][string]$Action = 'install',
    [string]$SkillsDir,
    [string]$Config,
    [string]$Python = 'python',
    [switch]$DryRun
)
$ErrorActionPreference = 'Stop'
$kitArgs = @('-B', (Join-Path $PSScriptRoot 'toolkit\cli.py'), $Action,
    '--agent', $Agent, '--scope', $Scope, '--skills', $Skills)
if ($Project) { $kitArgs += @('--project', $Project) }
if ($SkillsDir) { $kitArgs += @('--skills-dir', $SkillsDir) }
if ($Config) { $kitArgs += @('--config', $Config) }
if ($DryRun) { $kitArgs += '--dry-run' }
& $Python @kitArgs
exit $LASTEXITCODE
