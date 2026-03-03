import json
import pandas as pd
import requests
import streamlit as st
from pathlib import Path
from typing import Dict, Any

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2:1b"  # Mudar para um modelo real
DATA_PATH = Path(__file__).parent / "data"
TIMEOUT = 30  # segundos

# ============ FUNÇÕES DE CARREGAMENTO ============
@st.cache_data
def carregar_perfil() -> Dict:
    """Carrega perfil do investidor com segurança"""
    arquivo = DATA_PATH / "perfil_investidor.json"
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {arquivo}")
        return {}
    except json.JSONDecodeError:
        st.error(f"❌ Arquivo corrompido: {arquivo}")
        return {}

@st.cache_data
def carregar_transacoes() -> pd.DataFrame:
    """Carrega transações com segurança"""
    arquivo = DATA_PATH / "transacoes.csv"
    try:
        return pd.read_csv(arquivo)
    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {arquivo}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Erro ao ler transações: {e}")
        return pd.DataFrame()

@st.cache_data
def carregar_historico() -> pd.DataFrame:
    """Carrega histórico com segurança"""
    arquivo = DATA_PATH / "historico_atendimento.csv"
    try:
        return pd.read_csv(arquivo)
    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {arquivo}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"❌ Erro ao ler histórico: {e}")
        return pd.DataFrame()

@st.cache_data
def carregar_produtos() -> list:
    """Carrega produtos com segurança"""
    arquivo = DATA_PATH / "produtos_financeiros.json"
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"❌ Arquivo não encontrado: {arquivo}")
        return []
    except json.JSONDecodeError:
        st.error(f"❌ Arquivo corrompido: {arquivo}")
        return []

# ============ VERIFICAÇÃO DO OLLAMA ============
def verificar_ollama() -> bool:
    """Verifica se o servidor Ollama está rodando"""
    try:
        requests.get("http://localhost:11434/api/tags", timeout=2)
        return True
    except:
        return False

def listar_modelos_ollama() -> list:
    """Lista modelos disponíveis no Ollama"""
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        if r.status_code == 200:
            return [modelo['name'] for modelo in r.json().get('models', [])]
    except:
        pass
    return []

# ============ MONTAR CONTEXTO ============
def montar_contexto(perfil: Dict, transacoes: pd.DataFrame, 
                    historico: pd.DataFrame, produtos: list) -> str:
    """Monta o contexto de forma segura e limitada"""
    
    contexto = ""
    
    # Perfil
    if perfil:
        contexto += f"""
CLIENTE: {perfil.get('nome', 'N/A')}, {perfil.get('idade', 'N/A')} anos
PERFIL: {perfil.get('perfil_investidor', 'N/A')}
OBJETIVO: {perfil.get('objetivo_principal', 'N/A')}
PATRIMÔNIO: R$ {perfil.get('patrimonio_total', 0):.2f}
RESERVA: R$ {perfil.get('reserva_emergencia_atual', 0):.2f}

"""
    
    # Transações (limitar a 10)
    if not transacoes.empty:
        contexto += "TRANSAÇÕES RECENTES (últimas 10):\n"
        contexto += transacoes.head(10).to_string(index=False) + "\n\n"
    
    # Histórico (limitar a 5)
    if not historico.empty:
        contexto += "ÚLTIMOS ATENDIMENTOS:\n"
        contexto += historico.head(5).to_string(index=False) + "\n\n"
    
    # Produtos (apenas nomes e descrições resumidas)
    if produtos:
        contexto += "PRODUTOS DISPONÍVEIS (resumo):\n"
        for p in produtos[:5]:  # Limitar a 5 produtos
            contexto += f"- {p.get('nome')}: {p.get('categoria')} (risco {p.get('risco')})\n"
    
    return contexto

# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema finanças pessoais;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta, máximo 3 parágrafos.
"""

# ============ CHAMAR OLLAMA ============
def perguntar(msg: str, contexto: str) -> str:
    """Envia pergunta para o Ollama com tratamento de erros"""
    
    # Verifica Ollama
    if not verificar_ollama():
        return "❌ Ollama não está rodando! Por favor:\n1. Abra um terminal\n2. Execute: ollama serve\n3. Tente novamente"
    
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}
    """
    
    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "max_tokens": 500
                }
            },
            timeout=TIMEOUT
        )
        
        if r.status_code == 200:
            return r.json()['response']
        else:
            return f"❌ Erro {r.status_code}: {r.text}"
            
    except requests.exceptions.ConnectionError:
        return "❌ Não foi possível conectar ao Ollama. Verifique se ele está rodando."
    except requests.exceptions.Timeout:
        return "❌ Tempo limite excedido. Tente novamente."
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}"

# ============ INTERFACE STREAMLIT ============
def main():
    st.set_page_config(
        page_title="Edu - Educador Financeiro",
        page_icon="🎓",
        layout="wide"
    )
    
    st.title("🎓 Edu, o Educador Financeiro")
    
    # Barra lateral com status
    with st.sidebar:
        st.header("📊 Status")
        
        # Status do Ollama
        if verificar_ollama():
            st.success("✅ Ollama conectado")
            
            # Mostrar modelos disponíveis
            modelos = listar_modelos_ollama()
            if modelos:
                st.info(f"Modelos: {', '.join(modelos[:3])}")
        else:
            st.error("❌ Ollama desconectado")
            st.code("""
Para iniciar o Ollama:
1. Abra um terminal
2. Execute: ollama serve
            """)
        
        st.divider()
        
        # Carregar dados com feedback
        with st.spinner("Carregando dados..."):
            perfil = carregar_perfil()
            transacoes = carregar_transacoes()
            historico = carregar_historico()
            produtos = carregar_produtos()
        
        # Mostrar resumo dos dados
        st.header("📁 Dados Carregados")
        st.write(f"**Perfil:** {'✅' if perfil else '❌'}")
        st.write(f"**Transações:** {len(transacoes)} registros")
        st.write(f"**Histórico:** {len(historico)} registros")
        st.write(f"**Produtos:** {len(produtos)} disponíveis")
    
    # Inicializar histórico da conversa
    if "mensagens" not in st.session_state:
        st.session_state.mensagens = []
        st.session_state.contexto = montar_contexto(perfil, transacoes, historico, produtos)
    
    # Exibir mensagens anteriores
    for msg in st.session_state.mensagens:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
    
    # Input do usuário
    if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
        # Adicionar pergunta ao histórico
        st.session_state.mensagens.append({"role": "user", "content": pergunta})
        
        # Exibir pergunta
        with st.chat_message("user"):
            st.write(pergunta)
        
        # Gerar resposta
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                resposta = perguntar(pergunta, st.session_state.contexto)
                st.write(resposta)
        
        # Adicionar resposta ao histórico
        st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    
    # Sugestões iniciais
    if len(st.session_state.mensagens) == 0:
        st.info("""
        💡 **Sugestões de perguntas:**
        - O que é CDI?
        - Onde estou gastando mais?
        - Como funciona o Tesouro Selic?
        - O que é perfil moderado?
        - Como criar uma reserva de emergência?
        """)

if __name__ == "__main__":
    main()
