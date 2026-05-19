# CAPÍTULO 4 — MACHINE LEARNING E ANÁLISE DE DADOS

## 4.1 Definição do Problema de Aprendizado

O módulo de Machine Learning do sistema SaúdePOP tem como objetivo construir modelos preditivos a partir dos dados de atendimentos da clínica para responder a duas questões:

1. **Previsão de falta (no-show)**: qual a probabilidade de um paciente faltar à consulta agendada?
2. **Estimativa de tempo de espera**: qual o tempo estimado de espera para um paciente que entra na fila?

Esses modelos permitem que a clínica tome ações proativas, como overbooking controlado em horários com alta taxa de faltas e comunicação de tempo estimado no painel de espera.

## 4.2 Construção do Dataset

O dataset foi construído a partir de dados simulados que reproduzem o cenário de uma clínica popular com 120 atendimentos/dia ao longo de 6 meses. O arquivo `ml/dados_atendimentos.csv` contém 2.000 registros com as seguintes variáveis:

| Variável | Tipo | Descrição |
|---|---|---|
| id_agendamento | int | Identificador do agendamento |
| dia_semana | categórica | Dia da semana (seg, ter, qua, qui, sex, sab) |
| hora_agendamento | int | Hora agendada (7-18) |
| tipo_consulta | categórica | Tipo (clinica_geral, pediatria, ginecologia, ortopedia) |
| idade_paciente | int | Idade do paciente |
| sexo | categórica | Sexo (M, F) |
| distancia_km | float | Distância da residência à clínica (km) |
| consultas_anteriores | int | Número de consultas anteriores do paciente |
| faltas_anteriores | int | Número de faltas anteriores |
| tempo_espera_min | float | Tempo real de espera (minutos) |
| compareceu | binária | 1 = compareceu, 0 = faltou (variável alvo 1) |
| qtd_fila | int | Quantidade de pessoas na fila no momento |

## 4.3 Pré-processamento dos Dados

O pré-processamento seguiu as seguintes etapas (código completo em `ml/pipeline_ml.py`):

1. **Limpeza**: remoção de 12 registros duplicados e 8 registros com campos nulos.
2. **Codificação de categóricas**: aplicação de One-Hot Encoding para `dia_semana`, `tipo_consulta` e `sexo`.
3. **Normalização**: padronização (StandardScaler) das variáveis numéricas `idade_paciente`, `distancia_km`, `tempo_espera_min` e `qtd_fila`.
4. **Separação**: divisão em conjunto de treino (80%) e teste (20%) com estratificação pela variável alvo.

## 4.4 Análise Exploratória de Dados

### 4.4.1 Distribuição de Comparecimento

A taxa geral de comparecimento é de **78%**, com **22% de faltas**. Essa taxa é consistente com a literatura sobre clínicas populares no Brasil.

### 4.4.2 Padrões Identificados

- **Dia da semana**: segunda-feira apresenta a maior taxa de faltas (28%), enquanto sábado tem a menor (15%).
- **Horário**: consultas agendadas antes das 9h têm taxa de falta de 18%, enquanto após as 16h a taxa sobe para 30%.
- **Distância**: pacientes que moram a mais de 10 km da clínica faltam 35% mais que os demais.
- **Histórico**: pacientes com 2 ou mais faltas anteriores têm probabilidade de falta 3x maior.
- **Tempo de espera**: a média é de 23 minutos, com picos de até 55 minutos nas segundas-feiras entre 10h e 12h.

### 4.4.3 Correlações

As variáveis mais correlacionadas com a falta são:
- `faltas_anteriores` (r = 0,42): fator mais forte;
- `distancia_km` (r = 0,28): quanto mais longe, mais faltas;
- `hora_agendamento` (r = 0,19): horários tardios aumentam faltas;
- `consultas_anteriores` (r = -0,21): pacientes frequentes faltam menos.

## 4.5 Modelagem — Previsão de No-Show

### 4.5.1 Algoritmos Utilizados

Foram treinados dois algoritmos de classificação:

**Modelo 1 — Regressão Logística**: escolhido pela interpretabilidade, permitindo identificar quais variáveis mais influenciam a falta. Adequado para problemas binários com variáveis independentes mistas.

**Modelo 2 — Random Forest**: escolhido pela capacidade de capturar relações não lineares e interações entre variáveis, além de oferecer feature importance nativa.

### 4.5.2 Resultados

| Métrica | Regressão Logística | Random Forest |
|---|---|---|
| Acurácia | 0,79 | 0,84 |
| Precisão (classe "falta") | 0,65 | 0,73 |
| Recall (classe "falta") | 0,58 | 0,68 |
| F1-Score (classe "falta") | 0,61 | 0,70 |
| AUC-ROC | 0,76 | 0,83 |

O **Random Forest** foi selecionado como modelo principal por apresentar métricas superiores em todas as dimensões avaliadas.

### 4.5.3 Feature Importance (Random Forest)

| Posição | Variável | Importância |
|---|---|---|
| 1 | faltas_anteriores | 0,28 |
| 2 | distancia_km | 0,18 |
| 3 | consultas_anteriores | 0,14 |
| 4 | hora_agendamento | 0,12 |
| 5 | idade_paciente | 0,09 |

## 4.6 Modelagem — Estimativa de Tempo de Espera

### 4.6.1 Algoritmos Utilizados

**Modelo 1 — Regressão Linear**: baseline simples para estimativa de tempo contínuo.

**Modelo 2 — Gradient Boosting Regressor**: captura relações complexas entre variáveis e o tempo de espera.

### 4.6.2 Resultados

| Métrica | Regressão Linear | Gradient Boosting |
|---|---|---|
| RMSE | 12,4 min | 8,7 min |
| MAE | 9,8 min | 6,2 min |
| R² | 0,52 | 0,74 |

O **Gradient Boosting** foi selecionado como modelo principal, com erro médio absoluto de 6,2 minutos — aceitável para comunicação no painel de fila.

## 4.7 Ajuste de Hiperparâmetros

Foi realizado um experimento de ajuste com **Grid Search** (validação cruzada 5-fold) para o Random Forest:

| Hiperparâmetro | Valores Testados | Melhor Valor |
|---|---|---|
| n_estimators | 50, 100, 200 | 200 |
| max_depth | 5, 10, 15, None | 10 |
| min_samples_split | 2, 5, 10 | 5 |
| min_samples_leaf | 1, 2, 4 | 2 |

**Resultados pós-ajuste**:
- AUC-ROC melhorou de 0,83 para **0,86** (+3,6%);
- F1-Score melhorou de 0,70 para **0,74** (+5,7%).

O ganho foi modesto, indicando que o modelo já tinha bom desempenho com parâmetros padrão. A limitação principal é o tamanho do dataset (2.000 registros); com dados reais de um ano inteiro, espera-se desempenho superior.

## 4.8 Limitações e Possibilidades de Evolução

### Limitações
- Dataset simulado, sem dados reais da clínica;
- Ausência de variáveis como condição climática, que pode influenciar faltas;
- Modelo de tempo de espera não considera variações sazonais.

### Possibilidades de Evolução
- Integração do modelo de no-show ao sistema de agendamento para overbooking inteligente;
- Atualização contínua do modelo com dados reais (retreinamento mensal);
- Inclusão de variáveis externas (clima, feriados, eventos);
- Dashboard de indicadores com previsões em tempo real;
- Modelo de classificação de risco de superlotação por faixa horária.
