# CAPÍTULO 1 — ENGENHARIA DE SOFTWARE ÁGIL APLICADA

## 1.1 Visão e Escopo do Sistema

O sistema **SaúdePOP** é uma aplicação web projetada para resolver os problemas operacionais de clínicas populares, automatizando processos que hoje são manuais e propensos a erros.

### 1.1.1 Descrição do Problema

A Clínica Saúde Popular enfrenta os seguintes desafios:
- Prontuários em papel, sujeitos a perda e deterioração;
- Agendamentos em cadernos físicos, gerando conflitos de horários;
- Filas desorganizadas sem previsão de tempo de espera;
- Ausência de indicadores para tomada de decisão gerencial;
- Dificuldade de acesso rápido ao histórico clínico dos pacientes.

### 1.1.2 Atores Envolvidos

<img width="416" height="252" alt="Screenshot_89" src="https://github.com/user-attachments/assets/33384ccc-d01e-4a4e-82ad-c5610b8b82c0" />


### 1.1.3 Restrições

- O sistema deve funcionar em navegadores web modernos (Chrome, Firefox, Edge);
- Deve suportar acesso simultâneo de pelo menos 20 usuários;
- Os dados de saúde devem ser armazenados com criptografia;
- O sistema deve estar em conformidade com a LGPD (Lei Geral de Proteção de Dados).

## 1.2 Requisitos do Sistema

### 1.2.1 Requisitos Funcionais

<img width="604" height="537" alt="Screenshot_90" src="https://github.com/user-attachments/assets/abd1cd89-fb6d-4b85-9d2f-c5e99c624712" />


### 1.2.2 Requisitos Não Funcionais

<img width="579" height="330" alt="Screenshot_91" src="https://github.com/user-attachments/assets/d9fc7385-035e-412d-8d7d-5066f0bf9484" />


## 1.3 Backlog do Produto

O backlog foi organizado em formato de User Stories, priorizadas por valor para a clínica:

| # | User Story | Prioridade | Sprint |
|---|---|---|---|
| US01 | Como recepcionista, quero cadastrar pacientes para manter os dados atualizados | Alta | 1 |
| US02 | Como recepcionista, quero agendar consultas para organizar a agenda dos médicos | Alta | 1 |
| US03 | Como médico, quero acessar o prontuário do paciente para consultar o histórico | Alta | 1 |
| US04 | Como recepcionista, quero gerenciar a fila de espera para chamar pacientes na ordem | Alta | 2 |
| US05 | Como paciente, quero ver o painel da fila para saber minha posição | Média | 2 |
| US06 | Como médico, quero registrar o atendimento no prontuário eletrônico | Alta | 2 |
| US07 | Como recepcionista, quero realizar triagem do paciente antes da consulta | Média | 3 |
| US08 | Como administrador, quero ver relatórios de indicadores para tomar decisões | Média | 3 |
| US09 | Como administrador, quero controlar o acesso por perfis para garantir segurança | Alta | 3 |
| US10 | Como sistema, quero registrar logs de acesso ao prontuário para auditoria | Alta | 3 |

## 1.4 Planejamento de Sprints

### Sprint 1 — Fundação (2 semanas)
- **Objetivo**: Implementar cadastros básicos e estrutura do prontuário.
- **Itens**: US01, US02, US03.
- **Critérios de Aceite**: Pacientes e profissionais cadastrados; agendamento funcional; prontuário acessível por CPF.

### Sprint 2 — Fila e Atendimento (2 semanas)
- **Objetivo**: Implementar a gestão de fila e o registro de atendimentos.
- **Itens**: US04, US05, US06.
- **Critérios de Aceite**: Fila atualizada em tempo real; painel exibido na sala de espera; atendimento registrado com anamnese.

### Sprint 3 — Qualidade e Relatórios (2 semanas)
- **Objetivo**: Triagem, relatórios gerenciais e controle de acesso.
- **Itens**: US07, US08, US09, US10.
- **Critérios de Aceite**: Triagem registrada; relatórios gerados em PDF/tela; perfis de acesso funcionais; logs de auditoria gravados.

## 1.5 Quadro Kanban

O acompanhamento do projeto foi realizado por meio de um quadro Kanban com as colunas:

| A Fazer | Em Progresso | Em Revisão | Concluído |
|---|---|---|---|
| US07 | US06 | US04 | US01 |
| US08 | | US05 | US02 |
| US09 | | | US03 |
| US10 | | | |

## 1.6 Plano de Verificação e Validação

### 1.6.1 Estratégia de Testes

- **Testes Unitários**: validação individual das funções de cadastro, agendamento e fila (pytest).
- **Testes de Integração**: verificação da comunicação entre módulos (API ↔ Banco de Dados).
- **Testes de Aceitação**: validação com usuários simulados seguindo critérios de aceite das User Stories.

### 1.6.2 Casos de Teste

| ID | Caso de Teste | Resultado Esperado | Status |
|---|---|---|---|
| CT01 | Cadastrar paciente com dados válidos | Paciente salvo no banco e mensagem de sucesso | Aprovado |
| CT02 | Cadastrar paciente sem CPF | Mensagem de erro "CPF obrigatório" | Aprovado |
| CT03 | Agendar consulta em horário disponível | Agendamento criado com confirmação | Aprovado |
| CT04 | Agendar consulta em horário ocupado | Mensagem de erro "Horário indisponível" | Aprovado |
| CT05 | Adicionar paciente à fila de espera | Paciente aparece no painel de fila | Aprovado |
| CT06 | Chamar próximo paciente da fila | Status atualizado para "Em atendimento" | Aprovado |
| CT07 | Registrar atendimento no prontuário | Registro salvo com data/hora e profissional | Aprovado |
| CT08 | Consultar histórico do paciente | Lista de atendimentos exibida em ordem cronológica | Aprovado |

## 1.7 Aplicação das Práticas Ágeis e Qualidade

O projeto adotou o framework **Scrum** complementado por práticas de **Kanban** para visualização do fluxo de trabalho. As cerimônias ágeis incluíram planejamento de sprint, reuniões diárias (stand-ups) e retrospectivas ao final de cada sprint.

A qualidade foi assegurada por meio de:
- **Definição de Pronto (DoD)**: código revisado, testes passando, documentação atualizada;
- **Critérios de Aceite**: definidos para cada User Story antes do início do desenvolvimento;
- **Integração Contínua**: execução automatizada de testes a cada commit;
- **Revisão de Código**: toda alteração passa por revisão de pares antes de ser mesclada.

As normas de qualidade de software ISO/IEC 25010 foram consideradas para os atributos de funcionalidade, desempenho, segurança e usabilidade, orientando a definição dos requisitos não funcionais do sistema.
