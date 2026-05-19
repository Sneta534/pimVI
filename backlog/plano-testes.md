# Plano de Verificação e Validação — SaúdePOP

## 1. Estratégia de Testes

### 1.1 Níveis de Teste

| Nível | Ferramenta | Objetivo | Cobertura |
|---|---|---|---|
| **Unitário** | pytest | Validar funções individuais | Modelos, validações, utilitários |
| **Integração** | pytest + requests | Verificar comunicação entre módulos | API ↔ Banco de Dados |
| **Aceitação** | Manual / Checklist | Validar critérios de aceite das User Stories | Fluxos completos de uso |
| **Usabilidade** | Teste com usuários simulados | Avaliar facilidade de uso | Tarefas principais |

### 1.2 Critérios de Entrada e Saída

**Entrada**: Código implementado, ambiente de teste configurado, dados de teste inseridos.
**Saída**: Todos os casos de teste executados, bugs críticos corrigidos, relatório de teste gerado.

## 2. Casos de Teste

### 2.1 Módulo: Cadastro de Pacientes

| ID | Caso de Teste | Pré-condição | Passos | Resultado Esperado | Status |
|---|---|---|---|---|---|
| CT01 | Cadastrar paciente com dados válidos | Sistema acessível | 1. Acessar tela de cadastro<br>2. Preencher todos os campos obrigatórios<br>3. Clicar em "Salvar" | Paciente salvo no banco; mensagem "Paciente cadastrado com sucesso" | ✅ Aprovado |
| CT02 | Cadastrar paciente sem CPF | Sistema acessível | 1. Acessar tela de cadastro<br>2. Preencher campos sem CPF<br>3. Clicar em "Salvar" | Mensagem de erro "CPF é obrigatório" | ✅ Aprovado |
| CT03 | Cadastrar paciente com CPF duplicado | Paciente com mesmo CPF já cadastrado | 1. Acessar tela de cadastro<br>2. Inserir CPF já existente<br>3. Clicar em "Salvar" | Mensagem de erro "CPF já cadastrado" | ✅ Aprovado |
| CT04 | Buscar paciente por CPF | Paciente cadastrado | 1. Digitar CPF no campo de busca<br>2. Clicar em "Buscar" | Dados do paciente exibidos | ✅ Aprovado |

### 2.2 Módulo: Agendamento

| ID | Caso de Teste | Pré-condição | Passos | Resultado Esperado | Status |
|---|---|---|---|---|---|
| CT05 | Agendar consulta em horário disponível | Paciente e profissional cadastrados | 1. Selecionar paciente, profissional, consultório<br>2. Selecionar data/hora disponível<br>3. Clicar em "Agendar" | Agendamento criado com status "agendado" | ✅ Aprovado |
| CT06 | Agendar consulta em horário ocupado | Horário já possui agendamento | 1. Selecionar mesmo horário/profissional/consultório<br>2. Clicar em "Agendar" | Mensagem de erro "Horário indisponível" | ✅ Aprovado |
| CT07 | Cancelar agendamento | Agendamento existente | 1. Localizar agendamento<br>2. Clicar em "Cancelar"<br>3. Confirmar cancelamento | Status alterado para "cancelado" | ✅ Aprovado |
| CT08 | Visualizar agenda do dia | Agendamentos existentes | 1. Acessar dashboard<br>2. Selecionar data | Lista de agendamentos do dia exibida | ✅ Aprovado |

### 2.3 Módulo: Fila de Espera

| ID | Caso de Teste | Pré-condição | Passos | Resultado Esperado | Status |
|---|---|---|---|---|---|
| CT09 | Adicionar paciente à fila | Paciente com agendamento confirmado | 1. Buscar paciente<br>2. Selecionar consultório<br>3. Clicar em "Adicionar à Fila" | Paciente aparece na fila com status "aguardando" | ✅ Aprovado |
| CT10 | Chamar próximo paciente | Fila com pacientes aguardando | 1. Clicar em "Chamar Próximo" | Primeiro da fila muda para "chamado"; painel atualizado | ✅ Aprovado |
| CT11 | Prioridade na fila | Paciente prioritário na fila | 1. Adicionar paciente prioritário<br>2. Verificar posição | Paciente prioritário posicionado antes dos normais | ✅ Aprovado |
| CT12 | Painel de fila público | Fila com pacientes | 1. Acessar URL do painel (sem login) | Painel exibe nome do chamado e próximos | ✅ Aprovado |

### 2.4 Módulo: Prontuário Eletrônico

| ID | Caso de Teste | Pré-condição | Passos | Resultado Esperado | Status |
|---|---|---|---|---|---|
| CT13 | Registrar atendimento | Paciente na fila, chamado para consulta | 1. Acessar prontuário do paciente<br>2. Preencher anamnese e prescrição<br>3. Clicar em "Salvar" | Atendimento registrado com data/hora e profissional | ✅ Aprovado |
| CT14 | Consultar histórico de atendimentos | Paciente com atendimentos anteriores | 1. Buscar paciente por CPF<br>2. Acessar aba "Histórico" | Lista de atendimentos em ordem cronológica | ✅ Aprovado |
| CT15 | Registrar triagem | Atendimento em andamento | 1. Preencher PA, temperatura, peso, altura<br>2. Salvar | Dados de triagem vinculados ao atendimento | ✅ Aprovado |

### 2.5 Módulo: Segurança

| ID | Caso de Teste | Pré-condição | Passos | Resultado Esperado | Status |
|---|---|---|---|---|---|
| CT16 | Login com credenciais válidas | Usuário cadastrado | 1. Inserir login e senha<br>2. Clicar em "Entrar" | Redirecionado ao dashboard do perfil | ✅ Aprovado |
| CT17 | Login com credenciais inválidas | — | 1. Inserir login/senha incorretos<br>2. Clicar em "Entrar" | Mensagem "Usuário ou senha incorretos" | ✅ Aprovado |
| CT18 | Acesso restrito ao prontuário | Usuário com perfil "recepcionista" | 1. Tentar acessar tela de prontuário | Mensagem "Acesso negado" ou redirecionamento | ✅ Aprovado |
| CT19 | Geração de log de acesso | Médico acessa prontuário | 1. Acessar prontuário de um paciente | Log gerado automaticamente no MongoDB | ✅ Aprovado |

## 3. Resumo de Execução

| Módulo | Total de Casos | Aprovados | Reprovados | Taxa de Sucesso |
|---|---|---|---|---|
| Cadastro de Pacientes | 4 | 4 | 0 | 100% |
| Agendamento | 4 | 4 | 0 | 100% |
| Fila de Espera | 4 | 4 | 0 | 100% |
| Prontuário Eletrônico | 3 | 3 | 0 | 100% |
| Segurança | 4 | 4 | 0 | 100% |
| **Total** | **19** | **19** | **0** | **100%** |

## 4. Ferramentas Utilizadas

| Ferramenta | Finalidade |
|---|---|
| pytest | Execução de testes unitários e de integração |
| Postman | Testes manuais de API |
| Chrome DevTools | Inspeção de interface e rede |
| MongoDB Compass | Verificação de logs NoSQL |
