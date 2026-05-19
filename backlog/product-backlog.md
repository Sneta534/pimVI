# Product Backlog — SaúdePOP

## Visão do Produto

**Para** clínicas populares **que** enfrentam problemas com prontuários em papel, filas desorganizadas e falta de informações para gestão, **o** SaúdePOP **é** um sistema web **que** integra prontuário eletrônico, agendamento e fila inteligente. **Diferente de** soluções genéricas de gestão clínica, **nosso produto** é focado em simplicidade, baixo custo e adequação ao perfil de clínicas populares.

## Backlog Priorizado

### Épico 1: Cadastros Básicos

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US01 | Como recepcionista, quero cadastrar pacientes com dados pessoais para manter o registro atualizado | - Campos: nome, CPF, data nasc., telefone, e-mail, endereço<br>- CPF validado e único<br>- Mensagem de sucesso/erro | Alta | 1 | 5 |
| US02 | Como admin, quero cadastrar profissionais de saúde para vinculá-los ao sistema | - Campos: nome, CRM, especialidade, telefone, e-mail<br>- CRM único<br>- Flag ativo/inativo | Alta | 1 | 3 |
| US03 | Como admin, quero gerenciar consultórios para organizar o espaço | - Campos: número, andar, especialidade<br>- Número único | Média | 1 | 2 |

### Épico 2: Agendamento

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US04 | Como recepcionista, quero agendar consultas selecionando paciente, profissional, consultório e horário | - Verificar conflito de horário<br>- Status inicial "agendado"<br>- Mensagem de confirmação | Alta | 1 | 8 |
| US05 | Como recepcionista, quero visualizar a agenda do dia por profissional | - Listagem por data e profissional<br>- Status visual (ícones/cores) | Alta | 1 | 5 |

### Épico 3: Prontuário Eletrônico

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US06 | Como médico, quero acessar o prontuário do paciente para consultar o histórico clínico | - Busca por CPF ou nome<br>- Lista de atendimentos anteriores<br>- Detalhes de cada atendimento | Alta | 1 | 5 |
| US07 | Como médico, quero registrar o atendimento com anamnese e prescrição | - Campos: anamnese, prescrição (medicamento, dosagem, frequência), observações<br>- Registro com data/hora e profissional | Alta | 2 | 8 |
| US08 | Como recepcionista, quero registrar a triagem do paciente antes da consulta | - Campos: PA, temperatura, peso, altura<br>- Vinculado ao atendimento | Média | 3 | 3 |

### Épico 4: Fila Inteligente

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US09 | Como recepcionista, quero adicionar pacientes à fila de espera por consultório | - Seleção de consultório e paciente<br>- Posição automática<br>- Flag de prioridade | Alta | 2 | 5 |
| US10 | Como recepcionista ou médico, quero chamar o próximo paciente da fila | - Botão "Chamar Próximo"<br>- Atualização do painel<br>- Status muda para "chamado" | Alta | 2 | 5 |
| US11 | Como paciente, quero ver o painel da fila na sala de espera para saber minha posição | - Tela pública sem login<br>- Nome do chamado em destaque<br>- Lista dos próximos<br>- Tempo médio de espera | Média | 2 | 5 |

### Épico 5: Segurança e Auditoria

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US12 | Como admin, quero gerenciar usuários com perfis de acesso | - Perfis: recepcionista, médico, admin<br>- Ativar/desativar usuários<br>- Senha com hash | Alta | 3 | 5 |
| US13 | Como sistema, quero registrar logs de acesso ao prontuário | - Log automático a cada acesso<br>- Dados: usuário, paciente, ação, data/hora, IP<br>- Armazenado em MongoDB | Alta | 3 | 3 |

### Épico 6: Relatórios e Analytics

| ID | User Story | Critérios de Aceite | Prioridade | Sprint | Story Points |
|---|---|---|---|---|---|
| US14 | Como admin, quero ver relatórios de indicadores | - Total de atendimentos por período<br>- Taxa de faltas<br>- Tempo médio de espera<br>- Gráficos visuais | Média | 3 | 8 |
| US15 | Como admin, quero ver previsão de no-show | - Modelo ML integrado ao agendamento<br>- Indicador de risco por paciente | Baixa | Futuro | 13 |

## Resumo

| Sprint | User Stories | Total Story Points |
|---|---|---|
| Sprint 1 | US01, US02, US03, US04, US05, US06 | 28 |
| Sprint 2 | US07, US09, US10, US11 | 23 |
| Sprint 3 | US08, US12, US13, US14 | 19 |
| Futuro | US15 | 13 |
