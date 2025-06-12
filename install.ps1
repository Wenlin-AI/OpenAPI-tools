param(
    [string]$RepoDir = "OpenAPI-tools",
    [string]$Server = "token_counter"
)

$repoUrl = "https://github.com/Wenlin-AI/OpenAPI-tools"

if (-not (Test-Path (Join-Path $RepoDir ".git"))) {
    git clone $repoUrl $RepoDir
} else {
    git -C $RepoDir pull
}

Set-Location $RepoDir
& ./setup.ps1 $Server
