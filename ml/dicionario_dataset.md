# Dicionário do Dataset — dados_atendimentos.csv

## Descrição

Dataset simulado contendo 2.000 registros de agendamentos de consultas da Clínica Saúde Popular, representando 6 meses de operação. Os dados foram gerados para reproduzir padrões realistas de clínicas populares no Brasil.

## Variáveis

| # | Variável | Tipo | Valores | Descrição |
|---|---|---|---|---|
| 1 | id_agendamento | int | 1-2000 | Identificador único do agendamento |
| 2 | dia_semana | categórica | seg, ter, qua, qui, sex, sab | Dia da semana do agendamento |
| 3 | hora_agendamento | int | 7-18 | Hora agendada para a consulta |
| 4 | tipo_consulta | categórica | clinica_geral, pediatria, ginecologia, ortopedia | Especialidade da consulta |
| 5 | idade_paciente | int | 1-95 | Idade do paciente em anos |
| 6 | sexo | categórica | M, F | Sexo biológico do paciente |
| 7 | distancia_km | float | 0.5-30.0 | Distância da residência do paciente até a clínica (km) |
| 8 | consultas_anteriores | int | 0-15 | Número de consultas anteriores do paciente na clínica |
| 9 | faltas_anteriores | int | 0-8 | Número de faltas anteriores do paciente |
| 10 | qtd_fila | int | 0-20 | Quantidade de pessoas na fila no momento do agendamento |
| 11 | tempo_espera_min | float | 2.0-60.0 | Tempo real de espera em minutos (variável alvo para regressão) |
| 12 | compareceu | binária | 0 ou 1 | 1 = compareceu à consulta, 0 = faltou (variável alvo para classificação) |

## Distribuições

- **Taxa de comparecimento**: ~78% (compareceu=1)
- **Distribuição por sexo**: 42% masculino, 58% feminino
- **Idade média**: 45 anos (desvio padrão: 18)
- **Distância média**: 5,0 km (distribuição exponencial)
- **Tempo médio de espera**: 23 minutos

## Observações

- Os dados são **simulados** e não representam pacientes reais.
- As probabilidades de falta foram modeladas com base em literatura sobre absenteísmo em clínicas populares.
- O dataset pode ser regenerado executando `python ml/pipeline_ml.py` (a função `gerar_dataset()` é chamada automaticamente se o CSV não existir).
