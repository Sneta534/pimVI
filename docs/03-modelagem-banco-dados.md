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

## 2.2 Escolhas de Modelagem

### Entidades e Justificativas

O modelo relacional foi organizado em 8 entidades que refletem os processos operacionais da clínica popular:

- **Paciente**: Entidade central do sistema, contendo dados cadastrais. O CPF foi definido como UNIQUE para evitar duplicidade e servir como chave de busca rápida, atendendo ao fluxo da recepcionista que localiza pacientes por CPF.
- **Profissional**: Separada de Usuário para permitir que profissionais existam no sistema mesmo antes de terem login, e para que o CRM (registro de classe) seja gerenciado independentemente das credenciais de acesso.
- **Consultório** (equivalente a "Unidade" no contexto da clínica): Representa as salas físicas de atendimento. A tabela permite rastrear em qual consultório cada agendamento ocorre e organizar a fila por local, facilitando o encaminhamento do paciente.
- **Usuário**: Entidade de controle de acesso, vinculada opcionalmente a um Profissional (FK nullable). O campo `perfil` com CHECK constraint garante que apenas os papéis "recepcionista", "medico" e "admin" sejam aceitos.
- **Agendamento**: Liga paciente, profissional e consultório em um horário específico. O campo `status` com CHECK constraint controla o ciclo de vida: agendado → confirmado → realizado (ou falta/cancelado).
- **Atendimento**: Representa o prontuário eletrônico propriamente dito, com campos de anamnese e prescrição. A FK para Agendamento é nullable, pois atendimentos de emergência ou encaixe podem ocorrer sem agendamento prévio.
- **Triagem**: Separada do Atendimento em entidade própria (1:1) para manter os dados vitais (PA, temperatura, peso, altura) estruturados e facilitar consultas de acompanhamento ao longo do tempo, sem misturar com o texto livre do atendimento.
- **Fila**: Gerencia a fila de espera com suporte a prioridade numérica e status de chamada, permitindo o funcionamento do painel de sala de espera em tempo real.

### Normalização

O modelo foi normalizado até a **Terceira Forma Normal (3FN)**:

- **1FN** (atributos atômicos): Todos os campos são atômicos e indivisíveis. Não há grupos repetitivos. O endereço do paciente foi mantido como campo único VARCHAR(300) em vez de ser decomposto em rua, número, CEP etc., por decisão de simplicidade no cadastro rápido da recepção. A prescrição médica também é mantida como TEXT para flexibilidade, complementada pela anotação NoSQL para textos extensos.
- **2FN** (dependência funcional total): Todos os atributos não-chave dependem integralmente da chave primária composta ou simples. Na tabela AGENDAMENTO, por exemplo, `status` e `observacoes` dependem de `id_agendamento` como um todo, e não apenas de `id_paciente` ou `id_profissional` isoladamente.
- **3FN** (sem dependências transitivas): Eliminação de dependências transitivas. A `especialidade` do profissional é armazenada apenas na tabela PROFISSIONAL e nunca replicada em AGENDAMENTO ou ATENDIMENTO — obtida via JOIN quando necessário. Da mesma forma, os dados do paciente (nome, CPF) são referenciados por FK e nunca duplicados em FILA ou ATENDIMENTO.

### Pontos de Desnormalização

Foram adotados dois pontos de desnormalização intencional, justificados por requisitos de desempenho:

1. **Campo `posicao` na tabela FILA**: O número da posição na fila é armazenado diretamente e recalculado a cada inserção/remoção, em vez de ser derivado por `ROW_NUMBER()` a cada consulta. Justificativa: o painel de sala de espera consulta a fila a cada 5 segundos para todos os consultórios simultaneamente. Manter a posição pré-calculada evita a execução de window functions em queries de alta frequência, reduzindo a carga no banco de dados.

2. **Campo `especialidade` na tabela CONSULTÓRIO**: Embora a especialidade já exista na tabela PROFISSIONAL, ela também aparece no CONSULTÓRIO para permitir a exibição do painel de fila sem JOIN adicional com a tabela de profissionais. Essa redundância controlada é aceitável porque a especialidade de um consultório raramente muda.

### Índices Definidos

Os índices foram projetados para otimizar as três consultas mais críticas do sistema:

| Índice | Tabela | Coluna(s) | Justificativa |
|---|---|---|---|
| IX_Paciente_CPF | Paciente | cpf | Busca de paciente por CPF na recepção (operação mais frequente) |
| IX_Paciente_Nome | Paciente | nome | Busca alternativa por nome do paciente |
| IX_Agendamento_Data | Agendamento | data_hora | Listagem da agenda do dia (filtro por data) |
| IX_Agendamento_Paciente | Agendamento | id_paciente | Histórico de agendamentos de um paciente |
| IX_Agendamento_Status | Agendamento | status | Filtro de agendamentos por status (confirmados, faltas) |
| IX_Atendimento_Paciente | Atendimento | id_paciente | Recuperação do histórico de atendimentos |
| IX_Atendimento_Data | Atendimento | data_hora_inicio | Filtro de atendimentos por período |
| IX_Fila_Consultorio_Status | Fila | (id_consultorio, status) | Índice composto para listagem de fila por consultório com filtro de status — consulta mais frequente do painel de sala de espera |
| IX_Fila_Paciente | Fila | id_paciente | Verificação se paciente já está na fila |

A escolha dos índices priorizou as operações de leitura que ocorrem em alta frequência (painel de fila, busca de pacientes, agenda do dia), aceitando um custo marginalmente maior nas operações de escrita (INSERT/UPDATE).

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

<img width="660" height="185" alt="Screenshot_99" src="https://github.com/user-attachments/assets/5d15e122-11d7-4e21-b88a-a6e981c8c22c" />


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

### Modelo de Documento — Evento de Fila

```json
{
    "_id": "ObjectId('...')",
    "tipo": "evento_fila",
    "fila_id": 89,
    "paciente_id": 42,
    "consultorio_id": 1,
    "evento": "entrada",
    "posicao": 3,
    "data_hora": "2025-03-15T08:25:00Z",
    "detalhes": {
        "prioridade": 0,
        "qtd_fila_momento": 5,
        "tempo_estimado_min": 18
    }
}
```

### Justificativa da Escolha NoSQL

A escolha por MongoDB (NoSQL orientado a documentos) para esses três módulos justifica-se por:

1. **Flexibilidade de esquema**: Anotações livres de consulta não possuem estrutura fixa — cada profissional pode registrar informações diferentes (tags, anexos, campos variáveis). Um esquema relacional rígido exigiria campos opcionais excessivos ou tabelas de metadados complexas.

2. **Alto volume de logs**: O sistema de logs de acesso ao prontuário gera registros a cada visualização, edição ou impressão. O MongoDB suporta inserções de alta frequência com melhor desempenho que tabelas relacionais com muitas FKs e constraints.

3. **Consultas sem JOINs**: Os eventos de fila e logs de acesso são consultados isoladamente (por paciente, por data, por profissional) sem necessidade de JOINs com outras entidades. O modelo de documento permite armazenar toda a informação relevante em um único registro.

4. **Auditoria e conformidade (LGPD)**: Os logs de acesso ao prontuário atendem à necessidade de rastreabilidade exigida pela Lei Geral de Proteção de Dados, registrando quem acessou, quando e qual dado foi consultado.
