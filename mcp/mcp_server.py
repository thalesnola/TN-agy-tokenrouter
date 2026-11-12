import httpx
import json
import os
from typing import Dict, Any, Optional
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("Antigravity Ollama Router")

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
DEFAULT_FAST_MODEL = "qwen2.5-coder:7b"
DEFAULT_HEAVY_MODEL = "qwen3-coder:30b"

@mcp.tool()
async def ollama_status() -> str:
    """Check Ollama service status and list available local models."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{OLLAMA_BASE_URL}/api/tags")
            if resp.status_code == 200:
                models = [m["name"] for m in resp.json().get("models", [])]
                return f"Ollama is online at {OLLAMA_BASE_URL}. Available models: {', '.join(models)}"
            return f"Ollama responded with status code {resp.status_code}"
    except Exception as e:
        return f"Failed to connect to Ollama at {OLLAMA_BASE_URL}: {str(e)}"

@mcp.tool()
async def ollama_worker_task(prompt: str, model: str = DEFAULT_FAST_MODEL, system_prompt: Optional[str] = None) -> str:
    """
    Execute a routine worker task on a local Ollama model to save cloud tokens.
    
    Args:
        prompt: The task instructions or code prompt to execute.
        model: Model to use (default: qwen2.5-coder:7b or qwen3-coder:30b).
        system_prompt: Optional system instructions for the local worker.
    """
    try:
        payload: Dict[str, Any] = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }
        if system_prompt:
            payload["system"] = system_prompt

        async with httpx.AsyncClient(timeout=120.0) as client:
            resp = await client.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload)
            if resp.status_code == 200:
                result = resp.json()
                return result.get("response", "No response returned from model.")
            return f"Ollama error ({resp.status_code}): {resp.text}"
    except Exception as e:
        return f"Error communicating with local Ollama worker: {str(e)}"

@mcp.tool()
async def ollama_refactor(code: str, instructions: str, model: str = DEFAULT_HEAVY_MODEL) -> str:
    """
    Delegate code refactoring or heavy code generation to local Qwen model without consuming cloud quota.
    
    Args:
        code: Source code snippet or file content.
        instructions: Instructions on how to refactor or change the code.
        model: Model to use (default: qwen3-coder:30b for high intelligence).
    """
    prompt = f"### Existing Code:\n```\n{code}\n```\n\n### Refactoring Instructions:\n{instructions}\n\nPlease output the complete refactored code."
    system = "You are an expert AI software engineer executing a local code refactoring task."
    return await ollama_worker_task(prompt=prompt, model=model, system_prompt=system)

@mcp.tool()
async def ollama_code_review(code: str, model: str = DEFAULT_FAST_MODEL) -> str:
    """
    Perform a local code review and sanity check on code using Qwen coder model.
    
    Args:
        code: Code to review.
        model: Model to use (default: qwen2.5-coder:7b).
    """
    prompt = f"Please review the following code for potential bugs, security issues, and style improvements:\n\n```\n{code}\n```"
    system = "You are a senior code reviewer providing concise, actionable code feedback."
    return await ollama_worker_task(prompt=prompt, model=model, system_prompt=system)

LIGHTRAG_BASE_URL = os.getenv("LIGHTRAG_BASE_URL", "http://localhost:9621")

@mcp.tool()
async def lightrag_status() -> str:
    """Check LightRAG server status and health."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{LIGHTRAG_BASE_URL}/health")
            if resp.status_code == 200:
                data = resp.json()
                status = data.get("status", "unknown")
                llm = data.get("configuration", {}).get("llm_model", "unknown")
                embed = data.get("configuration", {}).get("embedding_model", "unknown")
                return f"LightRAG is online at {LIGHTRAG_BASE_URL} (Status: {status}). LLM: {llm}, Embeddings: {embed}."
            return f"LightRAG responded with status code {resp.status_code}"
    except Exception as e:
        return f"LightRAG server is offline or unreachable at {LIGHTRAG_BASE_URL}: {str(e)}"

@mcp.tool()
async def lightrag_query(query: str, mode: str = "hybrid") -> str:
    """
    Query the LightRAG Knowledge Graph and local vector store to retrieve structured multi-document intelligence without consuming cloud tokens.
    
    Args:
        query: Search question or investigation query.
        mode: Retrieval mode ('hybrid', 'local', 'global', 'naive', 'mix'). Default is 'hybrid'.
    """
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            payload = {"query": query, "mode": mode}
            resp = await client.post(f"{LIGHTRAG_BASE_URL}/query", json=payload)
            if resp.status_code == 200:
                data = resp.json()
                ans = data.get("response", "No answer found.")
                refs = data.get("references", [])
                ref_str = f"\n\nReferences: {', '.join(refs)}" if refs else ""
                return f"{ans}{ref_str}"
            return f"LightRAG query failed with status code {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error connecting to LightRAG at {LIGHTRAG_BASE_URL}: {str(e)}"

@mcp.tool()
async def lightrag_insert(text: str, source_name: str = "manual_input.txt") -> str:
    """
    Insert text or evidence into the LightRAG Knowledge Graph for persistent local extraction and indexing.
    
    Args:
        text: Text content or document snippet to index into the knowledge graph.
        source_name: Name or identifier of the source file/document.
    """
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            payload = {"text": text, "file_source": source_name}
            resp = await client.post(f"{LIGHTRAG_BASE_URL}/documents/text", json=payload)
            if resp.status_code == 200:
                data = resp.json()
                return f"Document accepted for LightRAG indexing (Track ID: {data.get('track_id', 'unknown')})."
            return f"LightRAG insert failed with status code {resp.status_code}: {resp.text}"
    except Exception as e:
        return f"Error connecting to LightRAG at {LIGHTRAG_BASE_URL}: {str(e)}"

if __name__ == "__main__":
    mcp.run()

