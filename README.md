# 🧠💳 Classificação Automática de Transações Bancárias (ETL + IA Generativa) 
### Pipeline completo em Python + Google Colab + OpenAI

Este projeto implementa um **pipeline ETL completo (Extract, Transform, Load)** combinado com um sistema robusto de classificação automática de transações bancárias usando **Regras Determinísticas + IA Generativa (OpenAI)**.

O objetivo é transformar extratos bancários crus em uma base de dados limpa, organizada e totalmente categorizada — ideal para dashboards, análises financeiras pessoais e projetos de ciência de dados.

---

# 📌 Funcionalidades do Projeto

✓ Conexão segura com Google Drive  
✓ Carregamento automático de CSV  
✓ Limpeza avançada das descrições  
✓ Padronização de datas e valores  
✓ Sistema de classificação híbrido:

1. 🔍 **Regras determinísticas por palavras-chave**  
2. 🤖 **Classificação via IA Generativa OpenAI (GPT)**  
3. 🧠 **Fallback heurístico inteligente**  
4. 🗃️ **Categoria final: Alimentação, Transporte, etc.**

✓ Visualizações estatísticas automáticas  
✓ Exportação final do dataset transformado  
✓ Código totalmente documentado para aprendizado


---

# 🎯 Objetivo do Projeto

Este projeto implementa um pipeline que:

✔ Lê um arquivo CSV contendo transações bancárias  
✔ Limpa, transforma e padroniza os dados  
✔ Usa IA generativa para **classificar automaticamente categorias** (ex.: supermercado, transporte, salário etc.)  
✔ Gera análises descritivas e gráficos  
✔ Exporta o dataset final enriquecido  

Esse tipo de solução é extremamente útil para:

- Melhoria da experiência do cliente  
- Sistemas de gestão financeira pessoal  
- Score de crédito  
- Monitoramento de gastos  
- Prevenção de fraudes  

---

# 🛠 Tecnologias Utilizadas

| Tecnologia | Função |
|-----------|--------|
| **Python 3** | Linguagem principal |
| **Pandas** | Manipulação de dados |
| **NumPy** | Processamento numérico |
| **Matplotlib / Seaborn** | Visualizações |
| **OpenAI API** | Classificação via IA |
| **Regex (re)** | Limpeza textual |
| **Google Drive + Colab** | Ambiente de execução |

---

# 🧱 Arquitetura do Projeto

           EXTRACT
             ↓
          TRANSFORM
             ↓
     IA GENERATIVA (LLM)
             ↓
      ANÁLISE E GRÁFICOS
             ↓
            LOAD


---
# 🤖 Classificação com IA (OpenAI + Regras) 
### O classificador funciona com um pipeline híbrido:

1. Regras determinísticas
Busca palavras-chave como "uber", "supermercado", "farmácia", etc.

2. IA Generativa (OpenAI)
Usa prompt com few-shot e resposta restrita.

3. Fallback heurístico
Analisa raízes de palavras.

5. Categoria Final
Se nada casar: Outros

---
# 📌 Categorias Utilizadas

- Transporte
- Moradia
- Educação
- Saúde
- Entretenimento
- Compras
- Salário
- Serviços
- Outros

---
# 🛠️ Como Funciona a Classificação por IA
O pipeline usa:
- Few-shot learning
- Prompt estrito
- Normalização de texto
- Verificação de acentos e variações
- Comparação exata e parcial

Isso garante uma classificação muito mais precisa do que abordagens simples.

---
# 🙋🏼‍♂️ Autor
Projeto desenvolvido por Alessandro Campos com foco em:
- Ciência de Dados
- Engenharia de Prompt
- ETL
- IA Generativa aplicada

Siga me também no linkedin
https://www.linkedin.com/in/alessandro-campos-60943231/

