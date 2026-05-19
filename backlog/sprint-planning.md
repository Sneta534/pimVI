# Planejamento de Sprints — SaúdePOP

## Metodologia

O projeto adota o framework **Scrum** com sprints de **2 semanas**, complementado por um quadro **Kanban** para visualização do fluxo de trabalho.

### Papéis e Responsabilidades

| Papel | Responsável | Responsabilidades |
|---|---|---|
| Product Owner | Professor orientador | Priorizar backlog, validar entregas |
| Scrum Master | Líder do grupo | Facilitar cerimônias, remover impedimentos |
| Time de Desenvolvimento | Membros do grupo | Desenvolver, testar e documentar |

### Cerimônias

| Cerimônia | Frequência | Duração | Objetivo |
|---|---|---|---|
| Sprint Planning | Início de cada sprint | 2h | Definir itens do sprint e plano de execução |
| Daily Standup | Diária | 15 min | Sincronizar progresso e identificar bloqueios |
| Sprint Review | Fim de cada sprint | 1h | Demonstrar incremento e coletar feedback |
| Sprint Retrospectiva | Fim de cada sprint | 1h | Identificar melhorias no processo |

---

## Sprint 1 — Fundação (Semanas 1-2)

### Objetivo
Implementar os cadastros básicos, o agendamento de consultas e o acesso ao prontuário do paciente.

### Itens do Sprint

| ID | User Story | Responsável | Status |
|---|---|---|---|
| US01 | Cadastro de pacientes | Dev 1 | Concluído |
| US02 | Cadastro de profissionais | Dev 1 | Concluído |
| US03 | Gestão de consultórios | Dev 2 | Concluído |
| US04 | Agendamento de consultas | Dev 2 | Concluído |
| US05 | Visualização da agenda do dia | Dev 3 | Concluído |
| US06 | Acesso ao prontuário do paciente | Dev 3 | Concluído |

### Definição de Pronto (DoD)
- Código implementado e funcionando
- Testes unitários passando
- Interface funcional e acessível
- Documentação atualizada

### Quadro Kanban — Final do Sprint 1

| A Fazer | Em Progresso | Em Revisão | Concluído |
|---|---|---|---|
| — | — | — | US01 ✓ |
| — | — | — | US02 ✓ |
| — | — | — | US03 ✓ |
| — | — | — | US04 ✓ |
| — | — | — | US05 ✓ |
| — | — | — | US06 ✓ |

### Velocidade: 28 story points

---

## Sprint 2 — Fila e Atendimento (Semanas 3-4)

### Objetivo
Implementar o registro de atendimentos no prontuário e a gestão de fila inteligente com painel de chamada.

### Itens do Sprint

| ID | User Story | Responsável | Status |
|---|---|---|---|
| US07 | Registro de atendimento (prontuário) | Dev 1 | Concluído |
| US09 | Adicionar paciente à fila | Dev 2 | Concluído |
| US10 | Chamar próximo paciente | Dev 2 | Concluído |
| US11 | Painel da sala de espera | Dev 3 | Concluído |

### Quadro Kanban — Final do Sprint 2

| A Fazer | Em Progresso | Em Revisão | Concluído |
|---|---|---|---|
| — | — | — | US07 ✓ |
| — | — | — | US09 ✓ |
| — | — | — | US10 ✓ |
| — | — | — | US11 ✓ |

### Velocidade: 23 story points

---

## Sprint 3 — Qualidade e Relatórios (Semanas 5-6)

### Objetivo
Implementar triagem, controle de acesso, logs de auditoria e relatórios gerenciais.

### Itens do Sprint

| ID | User Story | Responsável | Status |
|---|---|---|---|
| US08 | Triagem do paciente | Dev 1 | Concluído |
| US12 | Controle de acesso por perfis | Dev 2 | Concluído |
| US13 | Logs de auditoria (MongoDB) | Dev 3 | Concluído |
| US14 | Relatórios de indicadores | Dev 1 | Concluído |

### Quadro Kanban — Final do Sprint 3

| A Fazer | Em Progresso | Em Revisão | Concluído |
|---|---|---|---|
| — | — | — | US08 ✓ |
| — | — | — | US12 ✓ |
| — | — | — | US13 ✓ |
| — | — | — | US14 ✓ |

### Velocidade: 19 story points

---

## Burndown

| Sprint | Planejado | Entregue | Velocidade |
|---|---|---|---|
| Sprint 1 | 28 SP | 28 SP | 28 |
| Sprint 2 | 23 SP | 23 SP | 23 |
| Sprint 3 | 19 SP | 19 SP | 19 |
| **Total** | **70 SP** | **70 SP** | **média: 23,3** |
