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

if (-not (Test-Path ".venv")) {
    python -m venv .venv
}

& .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

if (-not (Test-Path ".env") -and (Test-Path ".env.example")) {
    Copy-Item ".env.example" ".env"
}

Write-Host "Setup complete" -ForegroundColor Green
