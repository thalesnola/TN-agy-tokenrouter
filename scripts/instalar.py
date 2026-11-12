#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instalador Multiplataforma (Windows / macOS / Linux) — antigravity-token-router v2.1.0
Configura a hierarquia em escada:
- Camada 1 (Cérebro): 1º Gemini 4 Argon -> 2º Claude Opus
- Camada 2 (Agentes Rápidos, sem limite de tamanho de arquivo): 1º Gemini 3.8 Flash -> 2º Claude Sonnet
- Camada 3 (Executores Locais Ollama): dsh-local, qwen-local, opencode-local, ollama-router
  (acionados pelo Cérebro ou distribuídos pelos Agentes Rápidos sob demanda do Cérebro)
"""
import os
import shutil
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    home = Path.home()
    gemini_cfg = home / ".gemini" / "config"
    agy_dir = home / ".gemini" / "antigravity"

    print("=" * 66)
    print("  Instalador Multiplataforma: antigravity-token-router (v2.1.0)")
    print("  Cérebro: Argon -> Opus | Rápidos: Flash 3.8 -> Sonnet | Ollama")
    print("=" * 66)

    # 1. Plugin token-router
    plugin_src = repo_root / "plugins" / "token-router"
    plugin_dst = gemini_cfg / "plugins" / "token-router"
    if plugin_src.exists():
        if plugin_dst.exists():
            shutil.rmtree(plugin_dst)
        shutil.copytree(plugin_src, plugin_dst)
        print(f"[+] Plugin token-router instalado em: {plugin_dst}")

    # 2. Skill model_router
    skill_dst = gemini_cfg / "skills" / "model_router"
    skill_dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_root / "skills" / "model-router-ollama" / "SKILL.md", skill_dst / "SKILL.md")
    print(f"[+] Skill model_router instalada em: {skill_dst / 'SKILL.md'}")

    # 3. AGENTS.md global
    gemini_cfg.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_root / "AGENTS.md", gemini_cfg / "AGENTS.md")
    print(f"[+] Regra global AGENTS.md atualizada em: {gemini_cfg / 'AGENTS.md'}")

    # 4. MCP ollama-router
    mcp_schemas_dst = agy_dir / "mcp" / "ollama-router"
    mcp_schemas_dst.mkdir(parents=True, exist_ok=True)
    for schema in (repo_root / "mcp" / "schemas").glob("*.json"):
        shutil.copy2(schema, mcp_schemas_dst / schema.name)

    mcp_srv_dst = agy_dir / "ollama_router"
    mcp_srv_dst.mkdir(parents=True, exist_ok=True)
    shutil.copy2(repo_root / "mcp" / "mcp_server.py", mcp_srv_dst / "mcp_server.py")
    shutil.copy2(repo_root / "mcp" / "requirements.txt", mcp_srv_dst / "requirements.txt")
    print(f"[+] Servidor e schemas MCP ollama-router instalados em: {mcp_srv_dst}")

    print("\nInstalação multiplataforma concluída com sucesso!")

if __name__ == "__main__":
    main()