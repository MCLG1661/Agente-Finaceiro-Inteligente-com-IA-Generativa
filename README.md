# 💰 Edu — Agente Financeiro Inteligente com IA Generativa

> Assistente de educação financeira contextual desenvolvido com **Python, Streamlit, Ollama e Llama 3.2**, utilizando dados estruturados, Context Engineering e guardrails para gerar respostas personalizadas com um LLM executado localmente.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000)
![Llama](https://img.shields.io/badge/Llama-3.2-0467DF)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![Generative AI](https://img.shields.io/badge/AI-Generative%20AI-8A2BE2)
![Context Engineering](https://img.shields.io/badge/AI-Context%20Engineering-7952B3)
![Local LLM](https://img.shields.io/badge/LLM-Local-success)
![DIO](https://img.shields.io/badge/DIO-Bradesco%20GenAI-5A0FC8)
![Status](https://img.shields.io/badge/Status-Protótipo-blue)

---

## 📌 Sobre o Projeto

O **Edu** é um protótipo de agente de Inteligência Artificial Generativa voltado à **educação financeira contextual**.

A aplicação combina um **LLM executado localmente** com diferentes fontes de dados estruturados para produzir explicações financeiras contextualizadas de acordo com informações disponíveis sobre um perfil demonstrativo.

O agente utiliza quatro dimensões principais de contexto:

```text
Perfil do Investidor
        +
Transações Financeiras
        +
Histórico de Atendimento
        +
Produtos Financeiros
        ↓
Context Engineering
        ↓
LLM Local
        ↓
Resposta Contextualizada
```

A solução foi desenvolvida com **Python e Streamlit**, utilizando **Ollama** para execução local do **Llama 3.2**.

Além da geração de respostas, o projeto explora conceitos importantes para aplicações baseadas em LLMs, como:

- Context Engineering;
- Prompt Engineering;
- guardrails;
- controle de escopo;
- tratamento de erros;
- limitação de contexto;
- dados estruturados;
- privacidade através de inferência local;
- experiência conversacional.

> ⚠️ **O Edu possui finalidade exclusivamente educacional e demonstrativa. Não realiza aconselhamento financeiro ou recomendação individual de investimentos.**

---

## 🎯 Objetivo

O objetivo do projeto é explorar como **Inteligência Artificial Generativa + dados estruturados + contexto** podem ser combinados para tornar uma experiência conversacional mais relevante.

Em vez de enviar apenas uma pergunta isolada ao modelo, o Edu constrói um contexto utilizando informações previamente disponíveis.

Isso permite investigar questões como:

- Como contextualizar respostas de um LLM?
- Como combinar diferentes fontes de dados em um prompt?
- Como limitar a quantidade de informação enviada ao modelo?
- Como estabelecer regras de comportamento para o agente?
- Como tratar perguntas fora do escopo?
- Como executar um modelo localmente?
- Como criar uma interface conversacional para o usuário?

---

# 💡 Problema

Assistentes baseados em LLMs podem produzir respostas genéricas quando recebem apenas uma pergunta sem contexto adicional.

Em educação financeira, uma explicação pode se tornar mais relevante quando considera informações como:

```text
Quem é o usuário?
        +
Qual é seu objetivo?
        +
Quais são suas transações?
        +
Quais interações já ocorreram?
        +
Quais informações financeiras estão disponíveis?
```

O Edu explora uma arquitetura em que essas informações são organizadas antes da interação com o modelo.

---

# 🧠 Arquitetura da Solução

```text
┌────────────────────────────┐
│          Usuário           │
│      Streamlit Chat        │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│          app.py            │
│ Orquestração da Aplicação  │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│     Carregamento de Dados  │
└─────────────┬──────────────┘
              │
     ┌────────┼─────────┬─────────┐
     ▼        ▼         ▼         ▼
  Perfil  Transações Histórico Produtos
   JSON      CSV       CSV       JSON
     │        │         │         │
     └────────┼─────────┼─────────┘
              ▼
┌────────────────────────────┐
│     Context Engineering    │
│      montar_contexto()     │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│       System Prompt        │
│ Regras + Escopo + Persona  │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│           Ollama           │
│       Llama 3.2:1b         │
│       Local Inference      │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│          Resposta          │
│       Contextualizada      │
└─────────────┬──────────────┘
              │
              ▼
┌────────────────────────────┐
│      Streamlit Chat        │
│       Resposta ao Usuário  │
└────────────────────────────┘
```

---

# 📚 Base de Contexto

O agente utiliza quatro conjuntos de dados demonstrativos.

## 👤 Perfil do Investidor

Arquivo:

[`data/perfil_investidor.json`](data/perfil_investidor.json)

Contém informações utilizadas para contextualização, como:

- idade;
- profissão;
- renda;
- perfil de investidor;
- objetivo principal;
- patrimônio;
- reserva de emergência;
- metas financeiras.

---

## 💳 Transações

Arquivo:

[`data/transacoes.csv`](data/transacoes.csv)

Representa um pequeno histórico demonstrativo de movimentações financeiras.

Entre as categorias presentes estão:

- receita;
- moradia;
- alimentação;
- lazer;
- saúde;
- transporte.

Essas informações permitem ao agente contextualizar perguntas relacionadas a organização financeira.

---

## 🗂️ Histórico de Atendimento

Arquivo:

[`data/historico_atendimento.csv`](data/historico_atendimento.csv)

Representa interações anteriores do usuário em diferentes canais e temas.

Exemplos de assuntos:

- CDB;
- Tesouro Selic;
- metas financeiras;
- atualização cadastral.

Esse conjunto demonstra como informações históricas podem contribuir para o contexto de uma experiência conversacional.

---

## 📊 Produtos Financeiros

Arquivo:

[`data/produtos_financeiros.json`](data/produtos_financeiros.json)

Contém informações demonstrativas sobre diferentes categorias de produtos financeiros, incluindo:

- Tesouro Selic;
- CDB;
- LCI/LCA;
- fundos.

Essas informações são utilizadas como **base educativa**, e não como mecanismo de recomendação financeira.

---

# 🔄 Context Engineering

Uma das partes centrais da implementação é a função:

```python
montar_contexto()
```

Ela consolida diferentes fontes antes de enviar a pergunta ao modelo.

Fluxo:

```text
perfil_investidor.json
          │
transacoes.csv
          │
historico_atendimento.csv
          │
produtos_financeiros.json
          │
          ▼
   montar_contexto()
          │
          ▼
Contexto Consolidado
          │
          ▼
     System Prompt
          │
          ▼
Pergunta do Usuário
          │
          ▼
         LLM
```

---

## 📏 Limitação de Contexto

O código não envia indiscriminadamente todos os registros ao modelo.

A implementação limita determinadas fontes:

```text
Transações → até 10 registros
Histórico → até 5 registros
Produtos → até 5 produtos
```

Isso demonstra um princípio importante de **Context Engineering**: selecionar e limitar informações relevantes antes da inferência.

---

# 🛡️ Guardrails

O agente utiliza um `SYSTEM_PROMPT` com regras explícitas de comportamento.

Entre elas:

- não recomendar investimentos específicos;
- responder apenas sobre finanças pessoais;
- utilizar os dados disponíveis como exemplos;
- adotar linguagem simples;
- admitir quando não possui determinada informação;
- manter respostas sucintas.

Fluxo conceitual:

```text
Pergunta
   ↓
System Prompt
   ↓
Regras de Comportamento
   ↓
Contexto Disponível
   ↓
LLM
   ↓
Resposta Controlada
```

Essas regras funcionam como **guardrails baseados em instruções**.

> O projeto não implementa uma camada independente e determinística de validação de segurança após a resposta do modelo. Os guardrails atuais são predominantemente definidos no prompt.

---

# 🤖 LLM Local com Ollama

O projeto utiliza **Ollama** para executar o modelo localmente.

Endpoint utilizado:

```text
http://localhost:11434/api/generate
```

Modelo configurado:

```text
llama3.2:1b
```

A aplicação também verifica se o servidor Ollama está disponível através de:

```text
http://localhost:11434/api/tags
```

Fluxo:

```text
Aplicação
   ↓
Ollama disponível?
   │
   ├── NÃO → Mensagem de erro
   │
   └── SIM
        ↓
      Prompt
        ↓
   Llama 3.2
        ↓
    Resposta
```

---

# 🔐 Privacidade e Inferência Local

Uma característica importante da arquitetura é a utilização de um modelo executado localmente.

```text
Dados Locais
     +
Aplicação Local
     +
Ollama
     +
LLM Local
```

Isso permite experimentar uma arquitetura em que a inferência não depende necessariamente de uma API externa de LLM.

Essa abordagem pode ser particularmente relevante para estudos envolvendo:

- privacidade;
- controle sobre os dados;
- experimentação offline;
- prototipação com modelos locais.

> A execução local do modelo não torna automaticamente uma aplicação segura ou adequada para produção. Segurança, governança, acesso aos dados e infraestrutura exigiriam controles adicionais em um cenário real.

---

# 💬 Interface Conversacional

A aplicação utiliza componentes de chat do Streamlit.

O usuário interage através de:

```python
st.chat_input()
```

e as mensagens são apresentadas através de:

```python
st.chat_message()
```

A interface também mantém as mensagens da sessão utilizando:

```python
st.session_state
```

Isso permite preservar visualmente a conversa enquanto a sessão do Streamlit estiver ativa.

---

# ⚙️ Tratamento de Erros

O código contempla diferentes cenários de falha.

### Dados

- arquivo inexistente;
- JSON inválido;
- erro na leitura de CSV.

### Ollama

- servidor indisponível;
- erro de conexão;
- timeout;
- status HTTP inesperado.

Fluxo:

```text
Operação
   ↓
Sucesso?
   │
   ├── SIM → Continua
   │
   └── NÃO
        ↓
 Tratamento de Exceção
        ↓
 Feedback ao Usuário
```

---

# 🛠️ Tecnologias

| Tecnologia | Aplicação |
|---|---|
| **Python** | Linguagem principal |
| **Streamlit** | Interface conversacional |
| **Ollama** | Execução local do LLM |
| **Llama 3.2** | Modelo de linguagem |
| **Pandas** | Processamento dos dados tabulares |
| **Requests** | Comunicação HTTP com Ollama |
| **JSON** | Perfil e catálogo de produtos |
| **CSV** | Transações e histórico |
| **Git** | Versionamento |
| **GitHub** | Repositório e documentação |

---

# 📂 Estrutura do Repositório

```text
Agente-Finaceiro-Inteligente-com-IA-Generativa/
│
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ Como Executar

## Pré-requisitos

Para executar o projeto são necessários:

- Python;
- Ollama;
- modelo Llama 3.2 disponível localmente.

---

## 1. Clone o repositório

```bash
git clone https://github.com/MCLG1661/Agente-Finaceiro-Inteligente-com-IA-Generativa.git

cd Agente-Finaceiro-Inteligente-com-IA-Generativa
```

---

## 2. Crie um ambiente virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Instale o Ollama

Instale o Ollama de acordo com seu sistema operacional.

Depois, obtenha o modelo utilizado pelo projeto:

```bash
ollama pull llama3.2:1b
```

---

## 5. Inicie o Ollama

Se necessário:

```bash
ollama serve
```

---

## 6. Execute a aplicação

Em outro terminal:

```bash
streamlit run app.py
```

O Streamlit abrirá a aplicação no navegador.

---

# 💬 Exemplos de Perguntas

A própria interface sugere perguntas como:

```text
O que é CDI?

Onde estou gastando mais?

Como funciona o Tesouro Selic?

O que é perfil moderado?

Como criar uma reserva de emergência?
```

Essas perguntas permitem explorar tanto conhecimento geral do modelo quanto o contexto estruturado fornecido pela aplicação.

---

# 🧩 Fluxo Completo

```text
Usuário
   ↓
Streamlit
   ↓
Pergunta
   ↓
Dados Estruturados
   │
   ├── Perfil
   ├── Transações
   ├── Histórico
   └── Produtos
   ↓
Context Engineering
   ↓
System Prompt + Guardrails
   ↓
Requests
   ↓
Ollama
   ↓
Llama 3.2
   ↓
Resposta
   ↓
Streamlit
   ↓
Usuário
```

---

# 💡 Competências Demonstradas

## Generative AI

- Large Language Models
- LLMs locais
- Generative AI
- Prompt Engineering
- Context Engineering
- Guardrails
- Conversational AI

## Python

- funções;
- tratamento de exceções;
- type hints;
- manipulação de arquivos;
- JSON;
- Pandas;
- requisições HTTP.

## Data

- dados estruturados;
- CSV;
- JSON;
- processamento tabular;
- construção de contexto a partir de múltiplas fontes.

## Aplicações de IA

- integração de LLM;
- inferência local;
- controle de contexto;
- tratamento de indisponibilidade do modelo;
- gerenciamento de sessão;
- interface conversacional.

## Engenharia

- Git;
- GitHub;
- organização de projeto;
- gerenciamento de dependências;
- documentação técnica.

---

# 💼 Aplicações Conceituais

Embora o projeto utilize educação financeira como domínio, a arquitetura pode ser adaptada conceitualmente para outros cenários.

### Customer Service

```text
Cliente
   +
Histórico
   +
Produtos
   +
Interações
   ↓
Contexto
   ↓
LLM
```

### Customer Success

```text
Perfil do Cliente
   +
Uso do Produto
   +
Histórico
   ↓
Assistente Contextual
```

### Marketing

```text
Cliente
   +
Comportamento
   +
Segmento
   +
Interações
   ↓
Experiência Personalizada
```

### Operações

```text
Dados Operacionais
   +
Procedimentos
   +
Histórico
   ↓
Assistente de Apoio
```

O padrão central é:

**Dados → Contexto → LLM → Resposta contextualizada**

---

# 🚀 Possíveis Evoluções

## Arquitetura

- separar interface, serviços e camada de dados;
- configuração através de variáveis de ambiente;
- API com FastAPI;
- Docker;
- persistência em banco de dados.

## IA

- RAG;
- embeddings;
- vector database;
- seleção dinâmica de contexto;
- diferentes modelos locais;
- function calling / tools;
- agentes especializados.

## Guardrails

- validação determinística de entrada;
- validação independente da saída;
- classificação de intenção;
- filtros de segurança;
- políticas de resposta estruturadas.

## Avaliação

- dataset de perguntas de teste;
- avaliação de factualidade;
- avaliação de grounding;
- testes de aderência aos guardrails;
- métricas de latência;
- comparação entre modelos.

## Observabilidade

- logging estruturado;
- monitoramento de erros;
- tempo de inferência;
- uso de contexto;
- rastreamento das interações.

---

# ⚠️ Limitações

O **Edu é um protótipo educacional e experimental**.

A aplicação:

- utiliza dados fictícios/demonstrativos;
- não deve ser utilizada para decisões financeiras reais;
- não substitui profissionais qualificados;
- não executa operações financeiras;
- não garante precisão das respostas geradas pelo LLM;
- não possui camada independente de validação das respostas;
- utiliza guardrails predominantemente baseados em prompt;
- depende de uma instância local do Ollama;
- não implementa RAG;
- não possui banco vetorial;
- não possui arquitetura de produção.

Essas limitações são importantes para distinguir o protótipo de uma aplicação financeira real.

---

# 🎓 Contexto Acadêmico

Projeto desenvolvido como **Desafio Final do Bootcamp GenAI — DIO / Bradesco**.

O desafio teve como objetivo explorar a criação de uma experiência digital de relacionamento financeiro utilizando **Inteligência Artificial Generativa, dados contextuais e boas práticas de experiência do usuário**.

**Professor:** Venilton Falvo Jr.

---

# 🙏 Agradecimentos

- **DIO**
- **Bradesco**
- **Prof. Venilton Falvo Jr.**

---

# 👨‍💻 Autor

**Marcus Guedes**

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

- **GitHub:** [MCLG1661](https://github.com/MCLG1661)
- **LinkedIn:** [Marcus Guedes](https://www.linkedin.com/in/marcusguedes/)

---

⭐ Se este projeto foi útil como referência para Generative AI, LLMs locais ou Context Engineering, considere deixar uma estrela no repositório.

💰 **Edu — transformando dados estruturados em contexto para experiências financeiras com IA Generativa.**
