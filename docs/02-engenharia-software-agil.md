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

### 1.1.2 Objetivos de Negócio

| # | Objetivo | Indicador de Sucesso |
|---|---|---|
| OBJ01 | Eliminar prontuários em papel | 100% dos atendimentos registrados eletronicamente |
| OBJ02 | Reduzir tempo de espera percebido | Painel de fila com tempo estimado visível aos pacientes |
| OBJ03 | Reduzir conflitos de agendamento | Zero conflitos de horário com detecção automática |
| OBJ04 | Garantir conformidade LGPD | 100% dos acessos ao prontuário registrados em log de auditoria |
| OBJ05 | Priorizar atendimento por legislação | Idosos, gestantes e PCDs chamados antes na fila automaticamente |
| OBJ06 | Fornecer indicadores gerenciais | Relatórios de faltas, tempo de espera e produtividade por profissional |

### 1.1.3 Atores Envolvidos

| Ator | Descrição | Principais Funcionalidades |
|---|---|---|
| **Paciente** | Pessoa que busca atendimento na clínica | Visualizar posição na fila (painel); consultar histórico |
| **Recepcionista** | Profissional responsável pelo balcão | Cadastrar pacientes; agendar consultas; gerenciar fila; buscar por CPF |
| **Profissional de Saúde** | Médico ou enfermeiro | Acessar prontuário; registrar atendimento; chamar próximo paciente |
| **Administrador** | Gestor da clínica | Cadastrar profissionais; gerenciar consultórios; visualizar relatórios |

### 1.1.4 Restrições

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

<img width="632" height="452" alt="Screenshot_92" src="https://github.com/user-attachments/assets/dd39e1b0-177d-4293-9f24-79901a402876" />


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

<img width="470" height="218" alt="Screenshot_93" src="https://github.com/user-attachments/assets/3b3c80fa-7238-4cd3-a6b5-271b01e605b4" />


## 1.6 Plano de Verificação e Validação

### 1.6.1 Estratégia de Testes

- **Testes Unitários**: validação individual das funções de cadastro, agendamento e fila (pytest).
- **Testes de Integração**: verificação da comunicação entre módulos (API ↔ Banco de Dados).
- **Testes de Aceitação**: validação com usuários simulados seguindo critérios de aceite das User Stories.

### 1.6.2 Casos de Teste

<img width="1055" height="447" alt="Screenshot_94" src="https://github.com/user-attachments/assets/93b89d44-34a4-4d1b-832c-68b50bf7fe7f" />


## 1.7 Evidências de Execução dos Testes

As evidências de execução dos testes foram coletadas durante o desenvolvimento e validação do sistema:

### Testes de API (via curl/Postman)

Exemplo de execução do teste CT01 (cadastro de paciente com dados válidos):

```bash
$ curl -X POST http://localhost:5000/api/pacientes \
  -H "Content-Type: application/json" \
  -d '{"nome":"Maria Silva","cpf":"123.456.789-00","telefone":"(11)99999-0001"}'

# Resposta (HTTP 201):
{"id_paciente":1,"nome":"Maria Silva","cpf":"123.456.789-00","created_at":"2026-05-20T00:08:56"}
```

Exemplo de execução do teste CT11 (prioridade na fila):

```bash
# Adicionar paciente normal (Maria)
$ curl -X POST http://localhost:5000/api/fila -H "Content-Type: application/json" \
  -d '{"id_paciente":1,"prioridade":"normal"}'
# Adicionar paciente prioritário (João)
$ curl -X POST http://localhost:5000/api/fila -H "Content-Type: application/json" \
  -d '{"id_paciente":2,"prioridade":"prioritario"}'
# Chamar próximo — João (prioritário) é chamado antes de Maria (normal)
$ curl -X POST http://localhost:5000/api/fila/chamar
# Resposta confirma: João Santos (id_paciente: 2) com status "chamado"
```

### Testes de Interface (Painel de Fila)

O painel de fila (`/painel`) foi verificado via navegador Chrome. A captura de tela confirma:
- Nome do paciente chamado em destaque (fonte grande, fundo azul)
- Lista de próximos pacientes visível
- Atualização automática a cada 5 segundos funcionando
- Contraste WCAG AAA (fundo escuro, texto branco)

> Capturas de tela das telas do sistema em funcionamento estão disponíveis em `ux/capturas/`.

### Resumo de Execução

| Módulo | Casos | Aprovados | Taxa |
|---|---|---|---|
| Cadastro de Pacientes | 4 | 4 | 100% |
| Agendamento | 4 | 4 | 100% |
| Fila de Espera | 4 | 4 | 100% |
| Prontuário Eletrônico | 3 | 3 | 100% |
| Segurança | 4 | 4 | 100% |
| **Total** | **19** | **19** | **100%** |

## 1.8 Aplicação das Práticas Ágeis, Normas e Modelos de Qualidade

### Framework Ágil Adotado

O projeto adotou o framework **Scrum** como metodologia principal de gestão, complementado por práticas de **Kanban** para visualização do fluxo de trabalho. A escolha do Scrum justifica-se pela natureza iterativa do projeto acadêmico, que permite entregas incrementais a cada sprint, e pela clareza dos papéis definidos (Product Owner, Scrum Master, Time de Desenvolvimento).

### Cerimônias Realizadas

As cerimônias ágeis foram conduzidas ao longo de 3 sprints de 2 semanas cada:

- **Sprint Planning**: No início de cada sprint, foram selecionados itens do backlog priorizado, estimados por Story Points usando a técnica de Planning Poker. A capacidade do time foi respeitada, mantendo a velocidade entre 19 e 28 story points por sprint.
- **Daily Standup**: Reuniões diárias de 15 minutos para sincronização do progresso, identificação de impedimentos e alinhamento entre os membros do time.
- **Sprint Review**: Ao final de cada sprint, o incremento foi demonstrado ao Product Owner (professor orientador), coletando feedback e validando os critérios de aceite.
- **Sprint Retrospectiva**: Reflexão sobre o processo, identificando pontos de melhoria. Por exemplo, na Sprint 1, identificou-se a necessidade de melhorar a documentação dos critérios de aceite, o que foi corrigido nas sprints seguintes.

### Artefatos Produzidos

| Artefato | Descrição | Localização |
|---|---|---|
| Product Backlog | 15 User Stories priorizadas por valor | `backlog/product-backlog.md` |
| Sprint Backlog | Itens selecionados para cada sprint com responsáveis | `backlog/sprint-planning.md` |
| Quadro Kanban | Colunas: A Fazer, Em Progresso, Em Revisão, Concluído | `backlog/sprint-planning.md` |
| Burndown Chart | Velocidade por sprint (28, 23, 19 SP) | `backlog/sprint-planning.md` |
| Definição de Pronto | Código revisado, testes passando, documentação atualizada | `backlog/sprint-planning.md` |

### Qualidade de Software — Normas Aplicadas

O projeto aplicou conceitos das seguintes normas e modelos de qualidade:

**ISO/IEC 25010 (Modelo de Qualidade de Produto de Software)**: Os requisitos não funcionais foram organizados segundo as características de qualidade desta norma:

| Característica ISO 25010 | Requisitos Relacionados | Como foi Aplicado |
|---|---|---|
| **Adequação Funcional** | RF01-RF12 | Todas as funcionalidades atendem aos requisitos especificados, validadas por 19 casos de teste |
| **Eficiência de Desempenho** | RNF01 (tempo de resposta ≤3s) | Operações de fila otimizadas com índices compostos no banco de dados |
| **Compatibilidade** | RNF05, RNF07 | Interface responsiva (min. 768px); suporte a 20 usuários simultâneos |
| **Usabilidade** | RNF05, RNF08 | Contraste WCAG AA; botões ≥44px; teste de usabilidade com 3 participantes |
| **Confiabilidade** | RNF04, RNF06 | Disponibilidade 99,5% em horário comercial; backup diário automatizado |
| **Segurança** | RNF02, RNF03 | Criptografia AES-256; conformidade LGPD; logs de auditoria obrigatórios |
| **Manutenibilidade** | — | Código modular (separação em models.py e app.py); documentação técnica |
| **Portabilidade** | — | Aplicação web acessível por qualquer navegador moderno; sem instalação local |

**ISO/IEC 12207 (Processos de Ciclo de Vida de Software)**: O ciclo de vida do projeto seguiu os processos de: levantamento de requisitos, projeto arquitetural, implementação, verificação (testes) e validação (demonstração ao PO).

**LGPD (Lei 13.709/2018)**: A conformidade com a Lei Geral de Proteção de Dados foi tratada como requisito transversal, implementada por meio de:
- Logs de acesso ao prontuário armazenados em MongoDB (rastreabilidade);
- Controle de acesso por perfis (apenas médicos acessam prontuários);
- Dados de saúde com indicação de criptografia (AES-256).

### Práticas de Engenharia Aplicadas

- **Definição de Pronto (Definition of Done)**: Todo item do backlog só foi considerado concluído quando: o código estava implementado e funcional, os testes passavam, a interface era acessível e a documentação estava atualizada.
- **Critérios de Aceite**: Definidos para cada User Story antes do desenvolvimento, servindo como base para os testes de aceitação. Exemplo: US09 (fila) exigia "flag de prioridade" e "posição automática".
- **Revisão de Código**: Todas as alterações passaram por revisão antes de serem integradas, garantindo consistência e qualidade do código.
- **Integração Contínua**: Testes unitários e de integração executados a cada commit para detecção precoce de regressões.

### Conclusão da Análise

A combinação de Scrum (para gestão iterativa), Kanban (para visualização de fluxo), ISO/IEC 25010 (para atributos de qualidade) e LGPD (para conformidade legal) proporcionou uma abordagem completa de engenharia de software. A velocidade média de 23,3 story points por sprint demonstra consistência do time, e a taxa de 100% de aprovação nos 19 casos de teste evidencia a eficácia do plano de verificação e validação adotado.
