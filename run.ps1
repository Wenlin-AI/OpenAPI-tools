param(
    [string]$Server = "token_counter"
)

$root = $PSScriptRoot
$serverPath = Join-Path $root "servers/$Server"
if (-not (Test-Path $serverPath)) {
    Write-Error "Server '$Server' not found"
    exit 1
}

Set-Location $serverPath

& .\.venv\Scripts\Activate.ps1

$settingsPath = Join-Path $root ".vscode/settings.json"
$host = "localhost"
$port = 8000
if (Test-Path $settingsPath) {
    $config = Get-Content $settingsPath | ConvertFrom-Json
    if ($config.local_server.host) { $host = $config.local_server.host }
    if ($config.local_server.port) { $port = $config.local_server.port }
}

uvicorn main:app --host $host --port $port
