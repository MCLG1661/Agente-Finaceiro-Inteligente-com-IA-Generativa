# 💰 Edu - Agente Financeiro Inteligente com IA Generativa

*Educação financeira contextual com Python, LLM local e dados estruturados*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Data%20App-FF4B4B?logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000)
![Llama](https://img.shields.io/badge/Llama-3.2-0467DF)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?logo=pandas&logoColor=white)
![Generative AI](https://img.shields.io/badge/Generative%20AI-Financial%20Education-8A2BE2)
![JSON](https://img.shields.io/badge/Data-JSON-000000?logo=json&logoColor=white)
![DIO](https://img.shields.io/badge/DIO-Bradesco%20GenAI-5A0FC8)
![Status](https://img.shields.io/badge/Status-Protótipo-blue)

O **Edu** é um protótipo de agente de IA Generativa voltado à **educação financeira contextual**.

O projeto foi desenvolvido como desafio final do **Bootcamp GenAI — DIO / Bradesco**, explorando como um modelo de linguagem executado localmente pode utilizar informações estruturadas para produzir explicações financeiras contextualizadas.

A solução combina **Python, dados JSON/CSV e um LLM executado via Ollama**, incorporando mecanismos de validação, contexto conversacional e tratamento de perguntas fora do escopo.

> ⚠️ O Edu possui finalidade educacional e demonstrativa. Não realiza consultoria financeira individualizada nem substitui profissionais qualificados.

---

## 🎯 Objetivo

Explorar a construção de um agente de IA capaz de utilizar contexto e dados estruturados para tornar explicações financeiras mais relevantes para diferentes situações.

O projeto trabalha conceitos como :

- Inteligência Artificial Generativa
- LLMs locais
- Context Engineering
- Prompt Engineering
- Dados estruturados
- Personalização de respostas
- Tratamento de edge cases
- Guardrails
- Privacidade
- Experiência conversacional

---

## 💡 Problema

Assistentes convencionais frequentemente respondem perguntas de maneira genérica.

Em educação financeira, entretanto, uma explicação pode se tornar mais útil quando considera informações contextuais.

O Edu explora uma arquitetura na qual :

```text
Pergunta
   ↓
Validação
   ↓
Contexto
   ↓
Dados disponíveis
   ↓
LLM
   ↓
Validação da resposta
   ↓
Explicação contextualizada

```
---

## ✨ Funcionalidades

💬 Assistente Conversacional

O usuário pode fazer perguntas relacionadas a conceitos e informações financeiras contempladas pelo escopo da aplicação.

🧠 Contextualização

O agente utiliza informações estruturadas para contextualizar suas respostas.

📊 Análise Educativa de Dados

Dados de transações podem ser utilizados para demonstrar padrões e apoiar explicações sobre organização financeira.

📚 Base de Produtos

Uma base estruturada permite ao agente consultar informações disponíveis sobre produtos financeiros para fins educativos.

🗂️ Histórico de Atendimento

O histórico permite explorar conceitos de continuidade e contexto em experiências conversacionais.

🛡️ Guardrails

O projeto contempla mecanismos para :

- Validar entradas
- Identificar perguntas fora do escopo
- Tratar tentativas de desvio das instruções
- Limitar respostas quando informações não estão disponíveis
- Reduzir respostas não fundamentadas

---

## 🏗️ Arquitetura

```text
Usuário
   ↓
Interface
   ↓
Validação de Entrada
   ↓
Detecção de Edge Cases
   ↓
Construção de Contexto
   ↓
┌─────────────────────────────┐
│ Dados estruturados          │
│                             │
│ • Perfil                    │
│ • Transações                │
│ • Histórico                 │
│ • Produtos                  │
└──────────────┬──────────────┘
               ↓
          Ollama
               ↓
        Llama 3.2
               ↓
     Geração da Resposta
               ↓
     Validação de Saída
               ↓
            Usuário

```

---

## 📚 Base de Conhecimento

O agente utiliza quatro conjuntos de dados estruturados :

`perfil_investidor.json` - Contextualização do perfil utilizado na demonstração

`transacoes.csv` - Histórico de transações

`historico_atendimento.csv` - Contexto de interações anteriores

`produtos_financeiros.json` - Informações sobre produtos disponíveis

Os dados utilizados fazem parte do ambiente demonstrativo do projeto.

---

## 🔐 Privacidade e Segurança

Um dos princípios explorados no projeto é a execução local do modelo por meio do **Ollama**.

A arquitetura também trabalha conceitos de :

- Validação de entrada
- Tratamento de edge cases
- Controle de escopo
- Validação das respostas
- Protocolo de ausência de informação
- Limitação de contexto
- Dados locais

O objetivo é experimentar práticas para tornar aplicações baseadas em LLMs mais controláveis e previsíveis.

---

## 🛠️ Tecnologias

**Python** - Desenvolvimento do agente

**Ollama** - Execução local do LLM

**Llama 3.2** - Modelo de linguagem 

**Pandas** - Processamento dos dados

**CSV** - Dados transacionais e históricos

**JSON** - Perfil e catálogo estruturado

**Streamlit** - Interface prevista/utilizada na experiência

---

## 📂 Estrutura Atual do Repositório

```text
Agente-Finaceiro-Inteligente-com-IA-Generativa/
│
├── src.py
├── perfil_investidor.json
├── produtos_financeiros.json
├── historico_atendimento.csv
├── transacoes.csv
└── README.md

```

---

## 🧠 Fluxo de Decisão

```text
Pergunta
   ↓
Entrada válida?
   ├── NÃO → Resposta de controle
   │
   └── SIM
        ↓
Informação disponível?
   ├── NÃO → Informa limitação
   │
   └── SIM
        ↓
Construção do contexto
        ↓
LLM
        ↓
Validação
        ↓
Resposta

```

---

## 💡 Competências Demonstradas

- Python
- Inteligência Artificial Generativa
- LLMs
- Ollama
- Llama
- Prompt Engineering
- Context Engineering
- Processamento de dados
- Pandas
- JSON e CSV
- Guardrails
- Tratamento de edge cases
- Arquitetura de agentes
- Privacidade em aplicações de IA
- Git e GitHub

---

## 🚀 Possíveis Evoluções

- Interface Streamlit completa
- Arquitetura modular
- Persistência de sessões
- Testes automatizados
- Avaliação sistemática das respostas
- Observabilidade
- Logs estruturados
- API com FastAPI
- Containerização com Docker
- Diferentes modelos locais
- RAG sobre conteúdos de educação financeira
- Avaliação de grounding e factualidade

---

## ⚠️ Escopo e Limitações

O **Edu é um projeto educacional e experimental**.

A aplicação foi desenvolvida para demonstrar conceitos relacionados a IA Generativa, contexto, dados estruturados e segurança de agentes.

O sistema :

- Não deve ser utilizado para decisões financeiras reais
- Não substitui orientação profissional
- Não garante resultados financeiros
- Trabalha com dados demonstrativos
- Possui escopo limitado às informações disponibilizadas ao agente

---

## 🎓 Contexto Acadêmico

Projeto desenvolvido como **Desafio Final do Bootcamp GenAI — DIO / Bradesco**.

O desafio teve como objetivo explorar a criação de uma experiência digital de relacionamento financeiro utilizando IA Generativa, dados contextuais e boas práticas de experiência do usuário.

---

## 🤝 Como Contribuir

Contribuições são bem-vindas, especialmente nas áreas de:

- LLMs locais
- Guardrails
- Avaliação de agentes
- RAG
- Prompt e Context Engineering
- UX conversacional
- APIs
- Testes
- Observabilidade

1. Faça um Fork do repositório
2. Crie uma branch para sua funcionalidade
3. Implemente e teste as alterações
4. Faça o commit
5. Envie sua branch
6. Abra um Pull Request descrevendo a contribuição

---

## 🙏 Agradecimentos
- DIO
- Bradesco
- Prof : Venilton Falvo Jr.

---

## 👨‍💻 Autor

**Marcus Guedes**

Marketing | Data Science | Inteligência Artificial | Gestão de Projetos

GitHub: MCLG1661

LinkedIn: Marcus Guedes

---

💰 **Edu — IA Generativa aplicada à educação financeira contextual.**
