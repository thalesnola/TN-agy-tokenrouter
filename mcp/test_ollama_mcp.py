import asyncio
import httpx
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

async def main():
    print(f"Testando conexao com Ollama em {OLLAMA_BASE_URL}...")
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if resp.status_code == 200:
                models = [m["name"] for m in resp.json().get("models", [])]
                print(f"[OK] Ollama ativo. Modelos disponiveis:\n  - " + "\n  - ".join(models))
            else:
                print(f"[ERRO] Resposta inesperada: {resp.status_code}")
    except Exception as e:
        print(f"[AVISO] Nao foi possivel conectar ao Ollama: {e}")

if __name__ == "__main__":
    asyncio.run(main())
