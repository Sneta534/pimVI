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

O dataset consolidado está em formato aberto (CSV) e acompanhado de um dicionário de dados detalhado (`ml/dicionario_dataset.md`). As variáveis de entrada incluem: horário e dia da semana do agendamento, tipo de consulta, histórico de faltas e consultas anteriores, distância da residência, idade e sexo do paciente, e quantidade de pessoas na fila.

## 4.3 Pré-processamento dos Dados

O pré-processamento seguiu as seguintes etapas (código completo no caderno Jupyter `ml/pipeline_ml.ipynb` e no script `ml/pipeline_ml.py`):

1. **Limpeza**: remoção de registros duplicados e registros com campos nulos, garantindo integridade dos dados para modelagem.
2. **Tratamento de valores ausentes**: verificação de nulos em todas as colunas com `isnull().sum()` e remoção dos registros afetados (estratégia adequada dado o volume do dataset).
3. **Codificação de variáveis categóricas**: aplicação de One-Hot Encoding (via `pd.get_dummies`) para as variáveis `dia_semana` (6 categorias), `tipo_consulta` (4 categorias) e `sexo` (2 categorias), com `drop_first=True` para evitar multicolinearidade.
4. **Normalização**: padronização (StandardScaler — média zero, desvio padrão unitário) das variáveis numéricas `idade_paciente`, `distancia_km`, `tempo_espera_min` e `qtd_fila`. A normalização é essencial para a Regressão Logística, que é sensível à escala das variáveis.
5. **Separação treino/teste**: divisão em conjunto de treino (80%) e teste (20%) com `random_state=42` para reprodutibilidade e estratificação pela variável alvo para manter a proporção de classes.

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

## 4.8 Limitações

1. **Dataset simulado**: Os dados foram gerados artificialmente, o que pode não capturar toda a complexidade de uma clínica real. As distribuições e correlações foram modeladas com base em literatura sobre absenteísmo em clínicas populares, mas padrões reais podem diferir significativamente.

2. **Variáveis externas ausentes**: Fatores como condições climáticas (chuva forte reduz comparecimento), feriados prolongados, greves de transporte público e eventos locais não foram incluídos no dataset, embora sejam relevantes no contexto de clínicas populares atendendo comunidades periféricas.

3. **Sazonalidade**: O modelo de tempo de espera não considera variações sazonais (por exemplo, aumento de demanda em períodos de surtos de gripe ou dengue), o que poderia ser tratado com variáveis adicionais de data.

4. **Tamanho do dataset**: Com 2.000 registros, o dataset é relativamente pequeno para técnicas de deep learning. Modelos como Random Forest e Gradient Boosting são mais adequados para esse volume, mas datasets maiores (12+ meses de operação real) permitiriam modelos mais robustos.

5. **Desbalanceamento de classes**: A taxa de falta de ~22% gera desbalanceamento moderado. Técnicas como SMOTE ou ajuste de pesos de classe poderiam melhorar o recall da classe minoritária (falta).

## 4.9 Possibilidades de Evolução

1. **Integração ao sistema de agendamento**: O modelo de no-show pode ser integrado à API do SaúdePOP para calcular o risco de falta em tempo real e sugerir overbooking controlado em horários com alta probabilidade de ausência.

2. **Retreinamento contínuo**: Com dados reais acumulados ao longo de meses de operação, o modelo pode ser retreinado periodicamente (mensal ou trimestral) para capturar mudanças nos padrões de comportamento.

3. **Variáveis externas**: Inclusão de dados climáticos (API de previsão do tempo), calendário de feriados e eventos locais para melhorar a acurácia das previsões.

4. **Modelo de superlotação**: Desenvolvimento de um terceiro modelo para classificar o risco de superlotação da clínica por faixa horária, combinando dados de agendamento, histórico de fila e previsões de no-show.

5. **Dashboard preditivo**: Criação de um painel com indicadores em tempo real mostrando previsões de falta, tempo estimado de espera e risco de superlotação, permitindo à gestão tomar ações preventivas.

6. **Notificação proativa**: Envio de lembretes personalizados (SMS/WhatsApp) para pacientes com alto risco de falta, priorizando aqueles identificados pelo modelo como mais propensos ao no-show.

## 4.10 Organização do Código

Todo o pipeline está organizado em dois formatos complementares:

- **Caderno Jupyter** (`ml/pipeline_ml.ipynb`): formato interativo com todas as etapas documentadas em células, desde a carga de dados até a avaliação final, permitindo execução passo a passo e visualização inline dos gráficos.
- **Script Python** (`ml/pipeline_ml.py`): formato executável para integração ao sistema e execução automatizada do pipeline completo.

Os resultados (gráficos e métricas) são salvos na pasta `ml/resultados/` para inclusão no relatório final.
