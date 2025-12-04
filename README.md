# 📘 ETL de Transações com IA Generativa  
### *Projeto de Portfólio – Bootcamp Santander Ciência de Dados*

Este projeto demonstra um pipeline **ETL completo (Extract, Transform, Load)** usando Python no Google Colab, com integração de **IA Generativa** para classificação automática de transações bancárias.

O objetivo é simular uma tarefa comum em instituições financeiras como o Santander: **categorizar automaticamente as despesas dos clientes**, gerando insights financeiros úteis e preparando dados para análises, dashboards e modelos de machine learning.

---

## 📑 Índice
1. [Objetivo do Projeto](#objetivo-do-projeto)  
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)  
3. [Arquitetura do Projeto](#arquitetura-do-projeto)  
4. [Estrutura de Pastas](#estrutura-de-pastas)  
5. [Dataset de Exemplo](#dataset-de-exemplo)  
6. [Executando o Notebook no Colab](#executando-o-notebook-no-colab)  
7. [Fluxo Completo do ETL](#fluxo-completo-do-etl)  
8. [Resultados Gerados](#resultados-gerados)  
9. [Possíveis Melhorias Futuras](#possíveis-melhorias-futuras)  
10. [Licença](#licença)

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

| Tecnologia | Uso |
|-----------|-----|
| **Python 3** | Linguagem principal |
| **Google Colab** | Ambiente de execução |
| **Pandas** | Manipulação de dados |
| **Matplotlib / Seaborn** | Visualização |
| **OpenAI API (IA Generativa)** | Classificação de transações |
| **python-dotenv** | Gerenciar credenciais |

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



### ETAPA 1 — Extract  
- Leitura do arquivo CSV  
- Validação dos campos  

### ETAPA 2 — Transform  
- Conversão de datas  
- Tratamento de valores  
- Limpeza das descrições  
- Padronização textual  

### ETAPA 3 — IA Generativa  
- Envio de prompts para classificar transações  
- Criação automática da coluna `category`  

### ETAPA 4 — Load  
- Exportação final para CSV  
- Dataset pronto para BI ou ML  

---

