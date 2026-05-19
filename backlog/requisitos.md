# Documento de Requisitos — SaúdePOP

## 1. Visão Geral

O sistema SaúdePOP é uma aplicação web para clínicas populares que integra prontuário eletrônico simplificado, agendamento de consultas e gestão de filas em tempo quase real.

## 2. Requisitos Funcionais

| ID | Requisito | Descrição | Prioridade |
|---|---|---|---|
| RF01 | Cadastro de Pacientes | Cadastrar, editar e buscar pacientes com CPF, nome, data de nascimento, telefone, e-mail e endereço | Alta |
| RF02 | Cadastro de Profissionais | Cadastrar profissionais de saúde com nome, CRM e especialidade | Alta |
| RF03 | Agendamento de Consultas | Agendar consultas com seleção de profissional, consultório, data e horário | Alta |
| RF04 | Prontuário Eletrônico | Registrar atendimentos com anamnese, prescrição e observações | Alta |
| RF05 | Gestão de Fila de Espera | Gerenciar fila por consultório com prioridade e status em tempo real | Alta |
| RF06 | Painel da Sala de Espera | Exibir painel público com nome do paciente chamado e próximos na fila | Média |
| RF07 | Histórico de Atendimentos | Consultar histórico completo de atendimentos por paciente | Alta |
| RF08 | Triagem | Registrar dados de triagem (PA, temperatura, peso, altura) | Média |
| RF09 | Relatórios Gerenciais | Gerar relatórios de atendimentos, faltas e tempos de espera | Média |
| RF10 | Controle de Acesso | Gerenciar usuários com perfis (recepcionista, médico, admin) | Alta |
| RF11 | Logs de Auditoria | Registrar logs de acesso ao prontuário para auditoria | Alta |
| RF12 | Busca por CPF | Buscar paciente rapidamente pelo CPF na recepção | Alta |

## 3. Requisitos Não Funcionais

| ID | Requisito | Categoria | Descrição |
|---|---|---|---|
| RNF01 | Tempo de Resposta | Desempenho | Tempo máximo de 3 segundos para qualquer operação |
| RNF02 | Criptografia | Segurança | Dados de saúde criptografados em repouso e em trânsito (HTTPS + AES-256) |
| RNF03 | LGPD | Segurança | Conformidade com a Lei Geral de Proteção de Dados Pessoais |
| RNF04 | Disponibilidade | Disponibilidade | 99,5% de disponibilidade em horário comercial (seg-sáb, 7h-19h) |
| RNF05 | Responsividade | Usabilidade | Interface funcional em tablets e desktops (min. 768px largura) |
| RNF06 | Backup | Confiabilidade | Backup automático diário do banco de dados |
| RNF07 | Concorrência | Escalabilidade | Suporte a 20 acessos simultâneos |
| RNF08 | Acessibilidade | Usabilidade | Contraste mínimo WCAG AA (4.5:1), botões ≥44px |

## 4. Regras de Negócio

| ID | Regra | Descrição |
|---|---|---|
| RN01 | Unicidade de CPF | Não pode haver dois pacientes com o mesmo CPF |
| RN02 | Conflito de Horário | Não pode agendar dois pacientes no mesmo horário, consultório e profissional |
| RN03 | Fila por Consultório | A fila é organizada por consultório, respeitando prioridade e ordem de chegada |
| RN04 | Prioridade na Fila | Pacientes idosos (≥60 anos), gestantes e PCD têm prioridade na fila |
| RN05 | Status de Agendamento | Status possíveis: agendado → confirmado → realizado / falta / cancelado |
| RN06 | Acesso ao Prontuário | Somente profissionais de saúde podem visualizar e editar prontuários |
| RN07 | Log Obrigatório | Todo acesso ao prontuário gera um registro de log (auditoria LGPD) |

## 5. Restrições Técnicas

- Banco de dados principal: SQL Server (relacional)
- Módulo de logs: MongoDB (NoSQL)
- Backend: Python (Flask)
- Frontend: HTML5, CSS3, JavaScript
- Compatibilidade: Chrome, Firefox e Edge (últimas 2 versões)
