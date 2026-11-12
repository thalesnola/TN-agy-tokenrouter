# Script deterministico para geracao de docs/diagrama-motion.svg
# Compativel 100% com sanitizador do GitHub (SVG Puro sem <filter> e sem style= inline)

import pathlib

SVG_CONTENT = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 920" width="1000" height="920">
  <defs>
    <!-- Degradê de fundo suave Motion -->
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#F3EEFF"/>
      <stop offset="50%" stop-color="#FFFFFF"/>
      <stop offset="100%" stop-color="#E9F7FF"/>
    </linearGradient>

    <!-- Ambient Glows em SVG Puro (substitui feGaussianBlur compatível com GitHub) -->
    <radialGradient id="glow_pink" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FF7AC6" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#FF7AC6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_blue" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2F9BFF" stop-opacity="0.22"/>
      <stop offset="100%" stop-color="#2F9BFF" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_purple" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow_green" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10B981" stop-opacity="0.20"/>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0"/>
    </radialGradient>

    <!-- Motion Trails Diagonais -->
    <linearGradient id="trail_purple" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#8A5CF6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#8A5CF6" stop-opacity="0.16"/>
      <stop offset="100%" stop-color="#8A5CF6" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="trail_blue" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3B82F6" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3B82F6" stop-opacity="0.14"/>
      <stop offset="100%" stop-color="#3B82F6" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <!-- Fundo -->
  <rect width="1000" height="920" fill="url(#bg)"/>

  <!-- Ambient Glows -->
  <circle cx="910" cy="110" r="230" fill="url(#glow_pink)"/>
  <circle cx="90" cy="790" r="250" fill="url(#glow_blue)"/>
  <circle cx="500" cy="330" r="280" fill="url(#glow_purple)"/>

  <!-- Motion Trails Diagonais (-12deg) -->
  <rect x="120" y="80" width="280" height="26" rx="13" fill="url(#trail_purple)" transform="rotate(-12 260 93)"/>
  <rect x="680" y="440" width="260" height="24" rx="12" fill="url(#trail_blue)" transform="rotate(-12 810 452)"/>
  <rect x="60" y="36" width="369.0" height="26" rx="13" fill="#EDE9FE" stroke="#DDD6FE" stroke-width="1"/>
  <text x="244.5" y="53" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="700" fill="#6D28D9" text-anchor="middle" letter-spacing="0.5">ROTEAMENTO EM ESCADA · PRESERVAÇÃO DE CONTEXTO</text><text x="60" y="86" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="26" font-weight="800" fill="#1B1F3B">TN-agy-tokenrouter · Roteador de Modelos no AGY</text><text x="60" y="114" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="14" font-weight="500" fill="#4A5568">Escada em 4 camadas: Cérebro Argon/Opus → Rápidos Flash/Sonnet → Locais Ollama → Bunker.</text>
  <rect x="62" y="158" width="880" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="154" width="880" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="150" width="880" height="72" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="74" y="162" width="165" height="20" rx="10" fill="#EDE9FE"/><text x="156" y="176" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#6D28D9" text-anchor="middle">1. CÉREBRO ORQUESTRADOR</text><text x="250" y="177" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Gemini 4 Argon → Claude Opus</text><text x="76" y="202" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#475569">Planejamento estratégico, arquitetura e trade-offs. Protegido contra leitura bruta (&gt; 3 arquivos).</text>
  <rect x="92" y="243" width="850" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="91" y="239" width="850" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="90" y="235" width="850" height="72" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="104" y="247" width="165" height="20" rx="10" fill="#E0F2FE"/><text x="186" y="261" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">2. AGENTES RÁPIDOS</text><text x="280" y="262" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Gemini 3.8 Flash → Claude Sonnet</text><text x="106" y="287" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#475569">SEM LIMITE DE LINHAS. Varre logs e bases de qualquer extensão e despacha tarefas mecânicas.</text>
  <rect x="122" y="328" width="820" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="121" y="324" width="820" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="120" y="320" width="820" height="72" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="134" y="332" width="165" height="20" rx="10" fill="#FEF3C7"/><text x="216" y="346" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#D97706" text-anchor="middle">3. EXECUTORES LOCAIS</text><text x="310" y="347" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Fila Serial Ollama (NUM_PARALLEL=1)</text><text x="136" y="372" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#475569">gpt-oss:20b (DSH), Qwen3-Coder-Next 36GB e Nemotron 30B sob mutex estrito a custo zero.</text>
  <rect x="152" y="413" width="790" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="151" y="409" width="790" height="72" rx="16" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="150" y="405" width="790" height="72" rx="16" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5"/><rect x="164" y="417" width="165" height="20" rx="10" fill="#F1F5F9"/><text x="246" y="431" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#475569" text-anchor="middle">4. CONTINGÊNCIA EM CAMADAS</text><text x="340" y="432" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Omni Route Combos + Bunker Offline</text><text x="166" y="457" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#475569">Intercepta HTTP 429 e comuta automaticamente sem interromper o trabalho do desenvolvedor.</text>
  <!-- BLOCO DE DEMONSTRAÇÃO PRÁTICA -->
  
  <rect x="62" y="563" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="61" y="559" width="880" height="220" rx="22" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="60" y="555" width="880" height="220" rx="22" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1.5"/>
  
  <rect x="80" y="569" width="225" height="24" rx="12" fill="#1B1F3B"/>
  <text x="192" y="585" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="800" fill="#60A5FA" text-anchor="middle" letter-spacing="0.8">DEMONSTRAÇÃO PRÁTICA</text>
  <text x="320" y="586" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="12" font-weight="600" fill="#64748B">Fluxo operacional concreto do repositório</text>
  
  <!-- Coluna 1: Entrada -->
  
  <rect x="84" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="83" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="82" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1.5"/>
  <rect x="94" y="617" width="90" height="20" rx="10" fill="#EDE9FE"/>
  <text x="139" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#7C3AED" text-anchor="middle">SOLICITAÇÃO EXTENSA</text>
  <text x="96" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Refatoração de 12 Arquivos</text>
  <text x="96" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="96" dy="0">Usuário solicita análise de 12</tspan><tspan x="96" dy="16">arquivos e 15.000 linhas de logs</tspan><tspan x="96" dy="16">para encontrar falha de concorrência.</tspan></text>
  
  <!-- Seta 1 -> 2 -->
  <circle cx="359" cy="682.5" r="14" fill="#EDE9FE" stroke="#C4B5FD" stroke-width="1.5"/>
  <text x="359" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#7C3AED" text-anchor="middle">→</text>
  
  <!-- Coluna 2: Processamento -->
  
  <rect x="379" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="378" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="377" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BAE6FD" stroke-width="1.5"/>
  <rect x="389" y="617" width="125" height="20" rx="10" fill="#E0F2FE"/>
  <text x="451" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#0284C7" text-anchor="middle">DISPERSÃO EM CAMADA</text>
  <text x="391" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Rápido + Executor Local</text>
  <text x="391" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="391" dy="0">Cérebro aciona Flash 3.8 (sem</tspan><tspan x="391" dy="16">limite de arquivo) que processa logs</tspan><tspan x="391" dy="16">e delega lote mecânico ao Qwen local.</tspan></text>
  
  <!-- Seta 2 -> 3 -->
  <circle cx="654" cy="682.5" r="14" fill="#E0F2FE" stroke="#7DD3FC" stroke-width="1.5"/>
  <text x="654" y="687.5" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#0284C7" text-anchor="middle">→</text>
  
  <!-- Coluna 3: Saída -->
  
  <rect x="674" y="613" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.06"/>
  <rect x="673" y="609" width="260" height="155" rx="14" fill="#1B1F3B" fill-opacity="0.05"/>
  <rect x="672" y="605" width="260" height="155" rx="14" fill="#FFFFFF" stroke="#BBF7D0" stroke-width="1.5"/>
  <rect x="684" y="617" width="105" height="20" rx="10" fill="#DCFCE7"/>
  <text x="736" y="631" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="10" font-weight="800" fill="#16A34A" text-anchor="middle">SÍNTESE EXECUTIVA</text>
  <text x="686" y="655" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#1B1F3B">Preservação de Janela</text>
  <text x="686" y="675" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="400" fill="#475569"><tspan x="686" dy="0">Cérebro recebe síntese limpa de</tspan><tspan x="686" dy="16">2 parágrafos com diff revisado,</tspan><tspan x="686" dy="16">economizando 95% dos tokens.</tspan></text>
  <!-- Faixa Navy Inferior de Conclusão Técnica -->
  <rect x="60" y="800" width="880" height="64" rx="18" fill="#1B1F3B"/>
  <circle cx="95" cy="832" r="15" fill="#3B82F6" fill-opacity="0.25"/>
  <text x="95" y="837" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="15" font-weight="800" fill="#60A5FA" text-anchor="middle">✓</text>
  <text x="125" y="829" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="13" font-weight="800" fill="#FFFFFF">Preservação Rigorosa de Janela e Cota</text>
  <text x="125" y="848" font-family="Segoe UI Variable Display, Segoe UI, sans-serif" font-size="11" font-weight="500" fill="#94A3B8">Arquitetura que protege a cognição dos modelos de topo enquanto executa tarefas volumosas com agilidade.</text>
</svg>'''

def main():
    p = pathlib.Path(__file__).parent.parent / 'docs' / 'diagrama-motion.svg'
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(SVG_CONTENT, encoding='utf-8')
    print('SVG gerado em:', p)

if __name__ == '__main__':
    main()
