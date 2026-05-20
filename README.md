# PIM VI — Sistema Ágil de Prontuário Eletrônico e Fila Inteligente para Clínicas Populares

**Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas**
**Universidade Paulista — UNIP EaD**

---

## Sobre o Projeto

Este repositório contém o Projeto Integrado Multidisciplinar VI (PIM VI), que propõe o desenho e a implementação de um ecossistema web para clínicas populares, integrando:

- **Prontuário eletrônico simplificado**
- **Agendamento de consultas**
- **Gestão de filas em tempo quase real**
- **Análise de dados e modelos preditivos**

O sistema foi projetado para a **Clínica Saúde Popular**, uma clínica fictícia que atende grande volume de pacientes com recursos administrativos limitados.

## Disciplinas Integradas

| Disciplina | Pasta | Descrição |
|---|---|---|
| Engenharia de Software Ágil Aplicada | `backlog/` | Requisitos, backlog, sprints, plano de testes |
| Modelagem de Banco de Dados e NoSQL | `database/` | Diagrama ER, DDL/DML SQL Server, esquema NoSQL |
| UX e UI Design | `ux/` | Personas, jornadas, wireframes, protótipo |
| Machine Learning e Análise de Dados | `ml/` | Dataset, pipeline ML, análise exploratória |

## Estrutura do Repositório

```
pimVI/
├── README.md                          # Este arquivo
├── docs/                              # Documento acadêmico (corpo do PIM)
│   ├── 01-introducao.md               # Introdução
│   ├── 02-engenharia-software-agil.md # Cap. 1 — Eng. de Software Ágil
│   ├── 03-modelagem-banco-dados.md    # Cap. 2 — Banco de Dados e NoSQL
│   ├── 04-ux-ui-design.md             # Cap. 3 — UX e UI Design
│   ├── 05-machine-learning.md         # Cap. 4 — Machine Learning
│   ├── 06-conclusao.md                # Conclusão
│   └── 07-referencias.md              # Referências bibliográficas (ABNT)
├── backlog/                           # Artefatos ágeis
│   ├── requisitos.md                  # Documento de requisitos
│   ├── product-backlog.md             # Backlog do produto
│   ├── sprint-planning.md             # Planejamento de sprints
│   └── plano-testes.md                # Plano de testes e evidências
├── database/                          # Banco de dados
│   ├── diagrama-er.md                 # Diagrama Entidade-Relacionamento
│   ├── dicionario-dados.md            # Dicionário de dados
│   ├── ddl.sql                        # Scripts DDL (SQL Server)
│   ├── dml.sql                        # Scripts DML (consultas e inserções)
│   └── nosql-schema.json              # Esquema e exemplos NoSQL
├── ux/                                # UX e UI Design
│   ├── personas.md                    # Personas do sistema
│   ├── jornadas.md                    # Mapas de jornada do usuário
│   ├── wireframes.md                  # Wireframes das telas principais
│   ├── teste-usabilidade.md           # Relatório de teste de usabilidade
│   ├── pesquisa-exploratoria.md       # Pesquisa exploratória (entrevistas, relatos)
│   ├── prototipo-navegavel.md         # Protótipo navegável com capturas de tela
│   └── capturas/                      # Capturas de tela do sistema
├── ml/                                # Machine Learning
│   ├── dados_atendimentos.csv         # Dataset simulado
│   ├── dicionario_dataset.md          # Dicionário do dataset
│   ├── pipeline_ml.py                 # Pipeline completo de ML (script)
│   ├── pipeline_ml.ipynb              # Pipeline completo de ML (Jupyter Notebook)
│   └── resultados/                    # Gráficos e resultados gerados
└── src/                               # Código-fonte da aplicação web
    ├── app.py                         # Aplicação principal (Flask)
    ├── models.py                      # Modelos de dados
    └── requirements.txt               # Dependências Python
```

## Como Montar o Documento Word (~20 páginas)

Para compilar o trabalho acadêmico, copie os arquivos da pasta `docs/` na ordem numérica:

1. **Capa** — conforme modelo do manual PIM VI
2. **Resumo / Abstract** — incluídos na introdução
3. **Sumário** — gerado automaticamente no Word
4. `docs/01-introducao.md` — Introdução (~1 página)
5. `docs/02-engenharia-software-agil.md` — Capítulo 1 (~5 páginas)
6. `docs/03-modelagem-banco-dados.md` — Capítulo 2 (~5 páginas)
7. `docs/04-ux-ui-design.md` — Capítulo 3 (~5 páginas)
8. `docs/05-machine-learning.md` — Capítulo 4 (~6 páginas)
9. `docs/06-conclusao.md` — Conclusão (~1 página)
10. `docs/07-referencias.md` — Referências

**Formatação**: Arial ou Times New Roman 12pt, espaçamento 1,5, margens 3cm (superior/esquerda) e 2cm (inferior/direita).

## Tecnologias Utilizadas

- **Backend**: Python (Flask)
- **Banco de Dados**: SQL Server (relacional) + MongoDB (NoSQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Python, Pandas, Scikit-learn, Matplotlib
- **Prototipagem**: Figma
- **Metodologia**: Scrum / Kanban

## Como Executar

```bash
# Instalar dependências
pip install -r src/requirements.txt

# Executar a aplicação
python src/app.py

# Executar pipeline de ML
python ml/pipeline_ml.py
```

---

*Projeto acadêmico desenvolvido para o PIM VI — UNIP EaD*
