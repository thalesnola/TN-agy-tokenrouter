# REGRAS OPERACIONAIS E ROTEAMENTO TÉCNICO NO ANTIGRAVITY

> **Diretriz Operacional:** Não há camada ou filtro automático de sigilo. O usuário é o único soberano e responsável pelo que decide inserir ou não na sessão de trabalho. O agente opera estritamente para **analisar a solicitação do usuário e distribuir a execução entre as camadas técnicas mais eficientes**.

---

# AMBIENTE WINDOWS, SHELL E FERRAMENTAS

- **Terminal no Windows (PowerShell 5.1 vs 7):**
  - ⚠️ No Windows o terminal abre no **Windows PowerShell 5.1**, onde **`&&` não existe** (erro de parser que rejeita a linha inteira).
  - Ao executar ou passar comandos compostos no PowerShell 5.1, use `;` entre comandos (ou chame `pwsh` para PowerShell 7) e use `git -C <dir>` no lugar de `cd <dir> && git ...`. Lembre que `;` não interrompe em caso de falha do comando anterior.
- **Gerenciador de Pacotes:** Chocolatey 2.7.3 em `C:\ProgramData\chocolatey`, `uv` 0.11 para ferramentas/MCPs Python, Node.js 24 LTS.
- **Grafo de Código/Projeto (Graphify):**
  - Existindo `graphify-out/graph.json`, consulte `graphify query "<pergunta>"` **antes** de ler arquivos; leia apenas o que o grafo apontar.
  - Após mudança relevante em projeto grande: `graphify . --update`.

---

# ROTEAMENTO AUTOMÁTICO DE MODELOS, ESCADA DE AGENTES & HIGIENE DE CONTEXTO

O agente principal atua obrigatoriamente como o **Cérebro Orquestrador**, operando em **hierarquia em escada**:

- **Camada 1 — Cérebro Orquestrador (em Escada: `ARGON` → `OPUS`):**
  1. **1º Degrau:** **`Gemini 4 Argon`** (modelo principal no Antigravity).
  2. **2º Degrau:** **`Claude Opus`** (`Opus 5.5` / `Opus`).
  - **Atribuição Exclusiva:** Análise do comando, planejamento estratégico, arquitetura, decisões de trade-off, redação final, síntese, edição direta de até 2 arquivos conhecidos e **comando para que os Agentes Rápidos distribuam tarefas aos modelos locais**.
- **Camada 2 — Agentes Rápidos (em Escada: `Flash 3.8` → `Sonnet`):**
  1. **1º Degrau:** **`Gemini 3.8 Flash`** (`Model: "flash"` via `invoke_subagent`).
  2. **2º Degrau:** **`Claude Sonnet`** (`Sonnet 5.5` / `Sonnet`).
  - **Sem Limite de Tamanho de Arquivo:** Os Agentes Rápidos (`Flash 3.8` e `Sonnet`) **NÃO possuem limite de tamanho de arquivo ou número de linhas**. Podem ler e processar arquivos, logs, CSVs ou módulos de qualquer extensão em seu próprio contexto isolado, devolvendo ao Cérebro apenas a síntese executiva limpa (1 a 3 parágrafos).
  - **Distribuição para Modelos Locais (sob demanda do Cérebro):** Os Agentes Rápidos **podem distribuir/despachar tarefas diretamente aos modelos locais do Ollama (Camada 3)** (`dsh-local`, `qwen-local`, `opencode-local`, MCP `ollama-router`), **desde que o Cérebro (`Argon` / `Opus`) demande expressamente essa distribuição**.

## 1. Gatilhos de Delegação e Distribuição

1. **Pesquisa em Codebase (> 3 arquivos) ou Leitura de Arquivos/Logs Volumosos:**
   - **Proibido** ler > 3 arquivos brutos ou despejar logs extensos diretamente na janela do Cérebro (`Argon` / `Opus`).
   - **Obrigatório** disparar Agente Rápido (`Gemini 3.8 Flash` → `Claude Sonnet`). Como os Agentes Rápidos **não têm limite de tamanho de arquivo**, eles processam o conteúdo integralmente e retornam apenas uma **síntese executiva limpa de 1 a 3 parágrafos** (amostra ≤ 3 linhas no console).

2. **Distribuição aos Executores Locais Ollama (Direta pelo Cérebro ou Distribuída pelos Agentes Rápidos sob Demanda do Cérebro):**
   - Quando o Cérebro (`Argon` / `Opus`) acionar diretamente ou **demandar que os Agentes Rápidos (`Flash 3.8` / `Sonnet`) distribuam** as tarefas aos modelos locais:
     - **`dsh-local` (`gpt-oss:20b` via DSH 0.2.0-rc.2):** código pequeno/médio (1–4 arquivos, ~70 s nesta máquina), ou revisão de segunda família local.
     - **`qwen-local` (`Qwen3-Coder-Next :NOTPL`, ~36 GB):** lote mecânico grande (≥ 5 arquivos, piso de 2–4 min por chamada — **nunca fatie**, envie o lote inteiro num único prompt).
     - **MCP `ollama-router`:** `ollama_refactor` (`qwen3-coder:30b`) para refatorações e `ollama_code_review` (`qwen2.5-coder:7b`) para revisões rápidas locais.
   - Todo trabalho de modelo local é **não revisado por definição** e deve ser conferido pelo Agente Rápido ou pelo Cérebro antes de integrar.

3. **Busca em Acervos e Memória de Longo Prazo:**
   - Acionar o **LightRAG** via `lightrag_query` (porta 9621 / Ollama local), ou o executor local **`opencode-local`** (`opencode run --agent investigador` com `nemotron-3.5-lightning:30b-a3b`) — diretamente ou via Agente Rápido sob demanda do Cérebro.

## 2. Regras do Ollama Local (workstation 16 — 64 GB RAM / RTX PRO 1000 8 GB)

- **Sempre o modelo mais completo instalado, nunca o reserva:** se faltar VRAM (< 13 GB livres), descarregue modelos residentes (`ollama stop <modelo>`) e mantenha o modelo principal (o Ollama divide camadas com a CPU).
- **Execução em série (`OLLAMA_NUM_PARALLEL=1`):** nunca rode dois pesos grandes simultaneamente (Qwen Code 36 GB e OpenCode Nemotron 25 GB são mutuamente exclusivos; confira `ollama ps`).
- **Variáveis de ambiente obrigatórias:** `OLLAMA_CONTEXT_LENGTH=32768`, `OLLAMA_FLASH_ATTENTION=1`, `OLLAMA_KV_CACHE_TYPE=q8_0`. Nunca usar `num_gpu: 0` (prefill cai 7×).

## 3. Ordem de Chaveamento de Contingência (Estouro de Tokens)

Caso os tokens do plano principal se esgotem ou ocorra bloqueio de taxa (HTTP 429):

1. **Escada do Cérebro e Agentes Rápidos:** Comutação na escada `Gemini 4 Argon` ↔ `Claude Opus` (Cérebro) e `Gemini 3.8 Flash` ↔ `Claude Sonnet` (Agentes Rápidos).
2. **PLANO A (Contingência Primária) — OMNI ROUTE:** Intercepta HTTP 429 e comuta via Routing Combos (`priority`) e compressão RTK.
3. **PLANO B (Contingência Secundária / Bunker Offline) — OLLAMA LOCAL:** Ativação imediata da MCP `ollama-router` (`qwen3-coder:30b` / `qwen2.5-coder:7b`), `claude-local`, **DSH** (`gpt-oss:20b`), **Qwen Code** (`Qwen3-Coder-Next:NOTPL`) e **OpenCode**, 100% offline a custo zero.
