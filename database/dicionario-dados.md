# Dicionário de Dados — SaúdePOP

## Tabela: Paciente
Armazena os dados cadastrais dos pacientes da clínica.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_paciente | INT | — | Não | IDENTITY | PK | Identificador único |
| nome | VARCHAR | 200 | Não | — | — | Nome completo do paciente |
| cpf | CHAR | 11 | Não | — | UNIQUE | CPF sem formatação |
| data_nascimento | DATE | — | Não | — | — | Data de nascimento |
| telefone | VARCHAR | 15 | Sim | NULL | — | Telefone com DDD |
| email | VARCHAR | 150 | Sim | NULL | — | E-mail de contato |
| endereco | VARCHAR | 300 | Sim | NULL | — | Endereço completo |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora do cadastro |

## Tabela: Profissional
Armazena os dados dos profissionais de saúde.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_profissional | INT | — | Não | IDENTITY | PK | Identificador único |
| nome | VARCHAR | 200 | Não | — | — | Nome completo |
| crm | VARCHAR | 20 | Não | — | UNIQUE | Registro CRM |
| especialidade | VARCHAR | 100 | Não | — | — | Especialidade médica |
| telefone | VARCHAR | 15 | Sim | NULL | — | Telefone |
| email | VARCHAR | 150 | Sim | NULL | — | E-mail |
| ativo | BIT | — | Não | 1 | — | Status ativo/inativo |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora do cadastro |

## Tabela: Consultorio
Armazena os consultórios disponíveis na clínica.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_consultorio | INT | — | Não | IDENTITY | PK | Identificador único |
| numero | INT | — | Não | — | UNIQUE | Número do consultório |
| andar | INT | — | Não | 1 | — | Andar |
| especialidade | VARCHAR | 100 | Sim | NULL | — | Especialidade atendida |
| ativo | BIT | — | Não | 1 | — | Status ativo/inativo |

## Tabela: Usuario
Armazena os usuários do sistema com controle de acesso.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_usuario | INT | — | Não | IDENTITY | PK | Identificador único |
| login | VARCHAR | 50 | Não | — | UNIQUE | Login de acesso |
| senha_hash | VARCHAR | 255 | Não | — | — | Hash da senha |
| perfil | VARCHAR | 20 | Não | — | CHECK | recepcionista, medico, admin |
| id_profissional | INT | — | Sim | NULL | FK | Vínculo com profissional |
| ativo | BIT | — | Não | 1 | — | Status ativo/inativo |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora do cadastro |

## Tabela: Agendamento
Armazena os agendamentos de consultas.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_agendamento | INT | — | Não | IDENTITY | PK | Identificador único |
| id_paciente | INT | — | Não | — | FK | Paciente agendado |
| id_profissional | INT | — | Não | — | FK | Profissional responsável |
| id_consultorio | INT | — | Não | — | FK | Consultório |
| data_hora | DATETIME | — | Não | — | — | Data/hora da consulta |
| status | VARCHAR | 20 | Não | 'agendado' | CHECK | agendado, confirmado, cancelado, realizado, falta |
| observacoes | VARCHAR | 500 | Sim | NULL | — | Observações |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora de criação |

## Tabela: Atendimento
Armazena os registros de atendimento (prontuário eletrônico).

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_atendimento | INT | — | Não | IDENTITY | PK | Identificador único |
| id_paciente | INT | — | Não | — | FK | Paciente atendido |
| id_profissional | INT | — | Não | — | FK | Profissional que atendeu |
| id_agendamento | INT | — | Sim | NULL | FK | Agendamento vinculado |
| data_hora_inicio | DATETIME | — | Não | — | — | Início do atendimento |
| data_hora_fim | DATETIME | — | Sim | NULL | — | Fim do atendimento |
| anamnese | TEXT | — | Sim | NULL | — | Anamnese do paciente |
| prescricao | TEXT | — | Sim | NULL | — | Prescrição médica |
| observacoes | VARCHAR | 500 | Sim | NULL | — | Observações |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora de criação |

## Tabela: Triagem
Armazena os dados de triagem do paciente antes da consulta.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_triagem | INT | — | Não | IDENTITY | PK | Identificador único |
| id_atendimento | INT | — | Não | — | FK | Atendimento vinculado |
| pressao_arterial | VARCHAR | 10 | Sim | NULL | — | PA (ex: 120/80) |
| temperatura | DECIMAL | 4,1 | Sim | NULL | — | Temperatura em °C |
| peso | DECIMAL | 5,2 | Sim | NULL | — | Peso em kg |
| altura | DECIMAL | 3,2 | Sim | NULL | — | Altura em metros |
| observacoes | VARCHAR | 500 | Sim | NULL | — | Observações |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora de criação |

## Tabela: Fila
Gerencia a fila de espera dos pacientes por consultório.

| Coluna | Tipo | Tamanho | Nulo | Padrão | Restrição | Descrição |
|---|---|---|---|---|---|---|
| id_fila | INT | — | Não | IDENTITY | PK | Identificador único |
| id_paciente | INT | — | Não | — | FK | Paciente na fila |
| id_consultorio | INT | — | Não | — | FK | Consultório destino |
| posicao | INT | — | Não | — | — | Posição atual na fila |
| status | VARCHAR | 20 | Não | 'aguardando' | CHECK | aguardando, chamado, em_atendimento, atendido, desistiu |
| hora_entrada | DATETIME | — | Não | — | — | Hora de entrada na fila |
| hora_chamada | DATETIME | — | Sim | NULL | — | Hora da chamada |
| prioridade | INT | — | Não | 0 | — | 0=normal, 1=prioritário |
| created_at | DATETIME | — | Não | GETDATE() | — | Data/hora de criação |
