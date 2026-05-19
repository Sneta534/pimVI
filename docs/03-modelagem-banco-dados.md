# CAPÍTULO 2 — MODELAGEM DE BANCO DE DADOS E NoSQL

## 2.1 Diagrama Entidade-Relacionamento

O modelo de dados do sistema SaúdePOP foi projetado para suportar as operações de cadastro de pacientes, profissionais de saúde, agendamentos, atendimentos e filas. O diagrama ER contempla as seguintes entidades e seus relacionamentos:

```
┌──────────────┐       ┌──────────────────┐       ┌──────────────────┐
│   PACIENTE   │       │   AGENDAMENTO    │       │  PROFISSIONAL    │
├──────────────┤       ├──────────────────┤       ├──────────────────┤
│ PK id_pacien │──┐    │ PK id_agendamen  │   ┌───│ PK id_profissio  │
│ nome         │  │    │ FK id_paciente   │───┘   │ nome             │
│ cpf (UNIQUE) │  └────│ FK id_profission │       │ crm              │
│ data_nascim  │       │ FK id_consultori │───┐   │ especialidade    │
│ telefone     │       │ data_hora        │   │   │ telefone         │
│ email        │       │ status           │   │   │ email            │
│ endereco     │       │ observacoes      │   │   │ ativo            │
│ created_at   │       │ created_at       │   │   │ created_at       │
└──────────────┘       └──────────────────┘   │   └──────────────────┘
       │                                      │
       │               ┌──────────────────┐   │
       │               │   CONSULTORIO    │───┘
       │               ├──────────────────┤
       │               │ PK id_consultor  │
       │               │ numero           │
       │               │ andar            │
       │               │ especialidade    │
       │               │ ativo            │
       │               └──────────────────┘
       │
       │       ┌──────────────────┐       ┌──────────────────┐
       │       │   ATENDIMENTO    │       │     TRIAGEM      │
       │       ├──────────────────┤       ├──────────────────┤
       └───────│ FK id_paciente   │       │ PK id_triagem    │
               │ PK id_atendimen │───────│ FK id_atendiment │
               │ FK id_profissio │       │ pressao_arterial │
               │ FK id_agendamen │       │ temperatura      │
               │ data_hora_inicio│       │ peso             │
               │ data_hora_fim   │       │ altura           │
               │ anamnese        │       │ observacoes      │
               │ prescricao      │       │ created_at       │
               │ observacoes     │       └──────────────────┘
               │ created_at      │
               └──────────────────┘
                       │
       ┌──────────────────┐       ┌──────────────────┐
       │      FILA        │       │     USUARIO      │
       ├──────────────────┤       ├──────────────────┤
       │ PK id_fila       │       │ PK id_usuario    │
       │ FK id_paciente   │       │ login            │
       │ FK id_consultori │       │ senha_hash       │
       │ posicao          │       │ perfil           │
       │ status           │       │ FK id_profission │
       │ hora_entrada     │       │ ativo            │
       │ hora_chamada     │       │ created_at       │
       │ prioridade       │       └──────────────────┘
       │ created_at       │
       └──────────────────┘
```

### Relacionamentos Principais

- **PACIENTE (1) → (N) AGENDAMENTO**: um paciente pode ter vários agendamentos.
- **PROFISSIONAL (1) → (N) AGENDAMENTO**: um profissional atende vários agendamentos.
- **CONSULTORIO (1) → (N) AGENDAMENTO**: cada agendamento ocorre em um consultório.
- **AGENDAMENTO (1) → (1) ATENDIMENTO**: cada agendamento pode gerar um atendimento.
- **ATENDIMENTO (1) → (1) TRIAGEM**: cada atendimento pode ter uma triagem associada.
- **PACIENTE (1) → (N) FILA**: um paciente pode entrar na fila várias vezes (em dias diferentes).
- **CONSULTORIO (1) → (N) FILA**: a fila é organizada por consultório.

## 2.2 Normalização

O modelo foi normalizado até a **Terceira Forma Normal (3FN)**:

- **1FN**: Todos os atributos são atômicos; não há grupos repetitivos. Exemplo: o endereço do paciente é um campo único de texto (sem subdivisões em tabelas separadas para CEP, rua etc.), decisão tomada para simplificar o cadastro rápido na recepção.
- **2FN**: Todos os atributos não-chave dependem integralmente da chave primária. Exemplo: na tabela AGENDAMENTO, o `status` depende de `id_agendamento`, não apenas de `id_paciente`.
- **3FN**: Não há dependências transitivas. Exemplo: `especialidade` do profissional está na tabela PROFISSIONAL, não se repete em ATENDIMENTO.

**Ponto de desnormalização**: O campo `posicao` na tabela FILA é recalculado a cada movimentação para evitar JOINs em consultas frequentes do painel de fila, priorizando desempenho de leitura.

## 2.3 Dicionário de Dados

### Tabela PACIENTE

<img width="600" height="354" alt="Screenshot_95" src="https://github.com/user-attachments/assets/643503bb-f926-4193-97cc-e4351775f15a" />


### Tabela PROFISSIONAL

<img width="602" height="363" alt="Screenshot_96" src="https://github.com/user-attachments/assets/258ba367-725b-4437-adf8-52989fe6a2fa" />


### Tabela AGENDAMENTO

<img width="669" height="313" alt="Screenshot_97" src="https://github.com/user-attachments/assets/d787a79d-a73a-4540-86d4-8b89021e9650" />


### Tabela FILA

<img width="687" height="351" alt="Screenshot_98" src="https://github.com/user-attachments/assets/53b7a1b3-b779-4723-94ff-f38391f7bebe" />


## 2.4 Scripts SQL Server (DDL)

Os scripts completos de criação do banco de dados estão disponíveis no arquivo `database/ddl.sql`. A seguir, um trecho representativo:

```sql
CREATE TABLE Paciente (
    id_paciente    INT IDENTITY(1,1) PRIMARY KEY,
    nome           VARCHAR(200)  NOT NULL,
    cpf            CHAR(11)      NOT NULL UNIQUE,
    data_nascimento DATE         NOT NULL,
    telefone       VARCHAR(15),
    email          VARCHAR(150),
    endereco       VARCHAR(300),
    created_at     DATETIME      DEFAULT GETDATE()
);

CREATE INDEX IX_Paciente_CPF ON Paciente(cpf);
```

### Índices Definidos

| Índice | Tabela | Coluna(s) | Justificativa |
|---|---|---|---|
| IX_Paciente_CPF | Paciente | cpf | Busca frequente por CPF na recepção |
| IX_Agendamento_Data | Agendamento | data_hora | Listagem de agenda do dia |
| IX_Fila_Consultorio | Fila | id_consultorio, status | Consulta da fila por consultório |
| IX_Atendimento_Paciente | Atendimento | id_paciente | Histórico de atendimentos |

## 2.5 Scripts SQL Server (DML)

Consultas representativas do sistema (arquivo completo em `database/dml.sql`):

```sql
-- Buscar paciente por CPF
SELECT * FROM Paciente WHERE cpf = '12345678901';

-- Listar fila atual do consultório 1, ordenada por prioridade e posição
SELECT f.posicao, p.nome, f.status, f.hora_entrada, f.prioridade
FROM Fila f
INNER JOIN Paciente p ON f.id_paciente = p.id_paciente
WHERE f.id_consultorio = 1 AND f.status IN ('aguardando', 'chamado')
ORDER BY f.prioridade DESC, f.posicao ASC;

-- Histórico de atendimentos de um paciente
SELECT a.data_hora_inicio, pr.nome AS profissional, pr.especialidade,
       a.anamnese, a.prescricao
FROM Atendimento a
INNER JOIN Profissional pr ON a.id_profissional = pr.id_profissional
WHERE a.id_paciente = 1
ORDER BY a.data_hora_inicio DESC;
```

## 2.6 Módulo NoSQL

Para complementar o modelo relacional, o sistema utiliza um módulo NoSQL baseado em documentos JSON (MongoDB) para armazenar:

- **Logs de acesso ao prontuário**: registro de quem acessou, quando e qual paciente;
- **Anotações livres de consulta**: textos não estruturados do profissional;
- **Eventos de atualização de fila**: histórico de movimentações para auditoria.

### Modelo de Documento — Log de Acesso

```json
{
    "_id": "ObjectId('...')",
    "tipo": "acesso_prontuario",
    "usuario_id": 5,
    "usuario_nome": "Dr. Carlos Silva",
    "paciente_id": 42,
    "paciente_cpf": "12345678901",
    "acao": "visualizacao",
    "data_hora": "2025-03-15T14:30:00Z",
    "ip_origem": "192.168.1.105",
    "detalhes": "Acesso ao histórico completo do paciente"
}
```

### Modelo de Documento — Anotação Livre

```json
{
    "_id": "ObjectId('...')",
    "tipo": "anotacao_consulta",
    "atendimento_id": 127,
    "profissional_id": 3,
    "data_hora": "2025-03-15T15:00:00Z",
    "conteudo": "Paciente relata melhora dos sintomas após tratamento...",
    "tags": ["acompanhamento", "melhora"]
}
```

### Consultas NoSQL Básicas

```javascript
// Buscar logs de acesso de um paciente específico
db.logs.find({ paciente_id: 42, tipo: "acesso_prontuario" })
       .sort({ data_hora: -1 });

// Contar acessos por profissional no último mês
db.logs.aggregate([
    { $match: { data_hora: { $gte: ISODate("2025-02-01") } } },
    { $group: { _id: "$usuario_nome", total: { $sum: 1 } } },
    { $sort: { total: -1 } }
]);

// Buscar anotações com tag específica
db.anotacoes.find({ tags: "acompanhamento" });
```

A escolha por NoSQL para esses registros justifica-se pela natureza flexível dos dados (anotações livres sem esquema fixo), pelo alto volume de logs gerados e pela facilidade de consultas por atributos variáveis, sem necessidade de JOINs complexos.
