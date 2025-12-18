# Análise Exploratória de Dados — Samsung Health

## 📌 Objetivo do projeto

Este projeto realiza uma **análise exploratória de dados (EDA)** a partir de métricas fisiológicas extraídas do Samsung Health, com foco em:

* Entender padrões e variações ao longo do tempo
* Comparar comportamentos entre diferentes períodos
* Investigar associações entre métricas fisiológicas
* Exercitar boas práticas de pré-processamento, análise exploratória e comunicação analítica

O escopo do projeto é **exploratório e analítico**, sem pretensão de modelagem preditiva ou inferência clínica.

---

## 📊 Fonte dos dados

Os dados utilizados são **dados pessoais**, exportados do Samsung Health e armazenados localmente em formato `.csv`.

> ⚠️ Observação importante
> Este projeto **não possui finalidade médica ou diagnóstica**. Todas as análises são exploratórias e devem ser interpretadas apenas como exercício analítico.

---

## 🧱 Estrutura do projeto

```
├── arquivos/
│   └── dados.csv
├── analise_exploratoria.ipynb
├── investigacao_preprocessamento.ipynb
├── preprocessamento.py
├── README.md
├── requirements.txt
├── .gitignore
```

### Descrição dos componentes

* **arquivos/**
  Contém os arquivos `.csv` utilizados como base de dados para as análises.

* **investigacao_preprocessamento.ipynb**
  Notebook exploratório inicial utilizado para:

  * compreender a estrutura bruta dos dados
  * identificar inconsistências
  * descobrir necessidades de limpeza, padronização e transformação

* **preprocessamento.py**
  Script responsável por aplicar o pré-processamento definido na etapa de investigação, permitindo:

  * reaproveitamento do código
  * separação clara entre preparação e análise
  * maior organização do fluxo analítico

* **analise_exploratoria.ipynb**
  Notebook principal de EDA, onde são realizadas:

  * análises estatísticas descritivas
  * visualizações orientadas por perguntas
  * comparações entre períodos e categorias
  * interpretações e conclusões exploratórias

* **requirements.txt**
  Lista de dependências do projeto, gerenciada pela biblioteca `uv`.

---

## 🔍 Metodologia

A abordagem adotada seguiu as seguintes etapas:

1. **Investigação inicial dos dados brutos**
2. **Definição e implementação do pré-processamento**
3. **Análise exploratória com foco em entendimento**
4. **Revisão crítica de hipóteses e descarte de análises pouco informativas**

As visualizações foram utilizadas como ferramentas de validação e entendimento, sempre associadas a perguntas analíticas específicas.

---

## 🧠 Principais aprendizados

* A importância de separar investigação, pré-processamento e análise
* A necessidade de contextualizar dados fisiológicos para evitar interpretações equivocadas
* O caráter iterativo da análise exploratória, que envolve testar e descartar hipóteses

---

## ⚠️ Limitações

* Fatores externos não controlados (rotina, sono, alimentação, estresse situacional)
* Ausência de validação clínica ou estatística inferencial avançada

Essas limitações são reconhecidas e fazem parte do escopo do projeto.