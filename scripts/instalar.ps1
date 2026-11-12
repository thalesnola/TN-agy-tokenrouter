# Instalador Completo Multi-Máquina: antigravity-token-router (Windows PowerShell 5.1 / 7)
# Instala a Hierarquia em Escada (Cérebro: Argon -> Opus | Rápidos: Flash 3.8 -> Sonnet | Locais: Ollama)

Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "  Instalador Multi-Máquina: antigravity-token-router (v2.1.0)     " -ForegroundColor Cyan
Write-Host "  Cérebro: Argon -> Opus | Rápidos: Flash 3.8 -> Sonnet | Ollama  " -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Split-Path -Parent $ScriptDir
$UserHome = $env:USERPROFILE

# 1. Instalar Plugin token-router completo em ~/.gemini/config/plugins/token-router
$PluginDest = Join-Path $UserHome ".gemini\config\plugins\token-router"
New-Item -ItemType Directory -Path $PluginDest -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "plugins\token-router\*") -Destination $PluginDest -Recurse -Force
Write-Host "[+] Plugin token-router (7 skills + rules + SVG) instalado em: $PluginDest" -ForegroundColor Green

# 2. Instalar Skill model_router em ~/.gemini/config/skills/model_router
$SkillDir = Join-Path $UserHome ".gemini\config\skills\model_router"
New-Item -ItemType Directory -Path $SkillDir -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "skills\model-router-ollama\SKILL.md") -Destination (Join-Path $SkillDir "SKILL.md") -Force
Write-Host "[+] Skill model_router instalada em: $SkillDir\SKILL.md" -ForegroundColor Green

# 3. Atualizar Regras Globais em ~/.gemini/config/AGENTS.md
$GlobalAgents = Join-Path $UserHome ".gemini\config\AGENTS.md"
New-Item -ItemType Directory -Path (Split-Path -Parent $GlobalAgents) -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "AGENTS.md") -Destination $GlobalAgents -Force
Write-Host "[+] Regras globais (Escada Argon->Opus / Flash 3.8->Sonnet) instaladas em: $GlobalAgents" -ForegroundColor Green

# 4. Instalar Schemas e Servidor MCP ollama-router
$McpSchemasDir = Join-Path $UserHome ".gemini\antigravity\mcp\ollama-router"
New-Item -ItemType Directory -Path $McpSchemasDir -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "mcp\schemas\*.json") -Destination $McpSchemasDir -Force

$OllamaServerDir = Join-Path $UserHome ".gemini\antigravity\ollama_router"
New-Item -ItemType Directory -Path $OllamaServerDir -Force | Out-Null
Copy-Item -Path (Join-Path $RepoRoot "mcp\mcp_server.py") -Destination (Join-Path $OllamaServerDir "mcp_server.py") -Force
Copy-Item -Path (Join-Path $RepoRoot "mcp\requirements.txt") -Destination (Join-Path $OllamaServerDir "requirements.txt") -Force
Write-Host "[+] Servidor e Schemas MCP ollama-router instalados em: $OllamaServerDir" -ForegroundColor Green

# 5. Configurar variáveis de ambiente recomendadas do Ollama no perfil do usuário (Windows)
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_PARALLEL", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_CONTEXT_LENGTH", "32768", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_FLASH_ATTENTION", "1", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_KV_CACHE_TYPE", "q8_0", "User")
Write-Host "[+] Variáveis do Ollama (NUM_PARALLEL=1, CTX=32768, FLASH_ATTN=1, KV=q8_0) configuradas!" -ForegroundColor Green

Write-Host "`nInstalação concluída com sucesso!" -ForegroundColor Cyan