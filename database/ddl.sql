-- =============================================================================
-- SaúdePOP — Sistema Ágil de Prontuário Eletrônico e Fila Inteligente
-- Scripts DDL — SQL Server
-- =============================================================================

-- Criação do banco de dados
CREATE DATABASE SaudePOP;
GO
USE SaudePOP;
GO

-- =============================================================================
-- Tabela: Paciente
-- =============================================================================
CREATE TABLE Paciente (
    id_paciente     INT IDENTITY(1,1) PRIMARY KEY,
    nome            VARCHAR(200)  NOT NULL,
    cpf             CHAR(11)      NOT NULL UNIQUE,
    data_nascimento DATE          NOT NULL,
    telefone        VARCHAR(15)   NULL,
    email           VARCHAR(150)  NULL,
    endereco        VARCHAR(300)  NULL,
    created_at      DATETIME      DEFAULT GETDATE()
);

CREATE INDEX IX_Paciente_CPF ON Paciente(cpf);
CREATE INDEX IX_Paciente_Nome ON Paciente(nome);

-- =============================================================================
-- Tabela: Profissional
-- =============================================================================
CREATE TABLE Profissional (
    id_profissional INT IDENTITY(1,1) PRIMARY KEY,
    nome            VARCHAR(200)  NOT NULL,
    crm             VARCHAR(20)   NOT NULL UNIQUE,
    especialidade   VARCHAR(100)  NOT NULL,
    telefone        VARCHAR(15)   NULL,
    email           VARCHAR(150)  NULL,
    ativo           BIT           DEFAULT 1,
    created_at      DATETIME      DEFAULT GETDATE()
);

-- =============================================================================
-- Tabela: Consultorio
-- =============================================================================
CREATE TABLE Consultorio (
    id_consultorio  INT IDENTITY(1,1) PRIMARY KEY,
    numero          INT           NOT NULL UNIQUE,
    andar           INT           DEFAULT 1,
    especialidade   VARCHAR(100)  NULL,
    ativo           BIT           DEFAULT 1
);

-- =============================================================================
-- Tabela: Usuario
-- =============================================================================
CREATE TABLE Usuario (
    id_usuario      INT IDENTITY(1,1) PRIMARY KEY,
    login           VARCHAR(50)   NOT NULL UNIQUE,
    senha_hash      VARCHAR(255)  NOT NULL,
    perfil          VARCHAR(20)   NOT NULL CHECK (perfil IN ('recepcionista', 'medico', 'admin')),
    id_profissional INT           NULL,
    ativo           BIT           DEFAULT 1,
    created_at      DATETIME      DEFAULT GETDATE(),
    CONSTRAINT FK_Usuario_Profissional FOREIGN KEY (id_profissional)
        REFERENCES Profissional(id_profissional)
);

-- =============================================================================
-- Tabela: Agendamento
-- =============================================================================
CREATE TABLE Agendamento (
    id_agendamento  INT IDENTITY(1,1) PRIMARY KEY,
    id_paciente     INT           NOT NULL,
    id_profissional INT           NOT NULL,
    id_consultorio  INT           NOT NULL,
    data_hora       DATETIME      NOT NULL,
    status          VARCHAR(20)   DEFAULT 'agendado'
        CHECK (status IN ('agendado', 'confirmado', 'cancelado', 'realizado', 'falta')),
    observacoes     VARCHAR(500)  NULL,
    created_at      DATETIME      DEFAULT GETDATE(),
    CONSTRAINT FK_Agendamento_Paciente FOREIGN KEY (id_paciente)
        REFERENCES Paciente(id_paciente),
    CONSTRAINT FK_Agendamento_Profissional FOREIGN KEY (id_profissional)
        REFERENCES Profissional(id_profissional),
    CONSTRAINT FK_Agendamento_Consultorio FOREIGN KEY (id_consultorio)
        REFERENCES Consultorio(id_consultorio)
);

CREATE INDEX IX_Agendamento_Data ON Agendamento(data_hora);
CREATE INDEX IX_Agendamento_Paciente ON Agendamento(id_paciente);
CREATE INDEX IX_Agendamento_Status ON Agendamento(status);

-- =============================================================================
-- Tabela: Atendimento
-- =============================================================================
CREATE TABLE Atendimento (
    id_atendimento  INT IDENTITY(1,1) PRIMARY KEY,
    id_paciente     INT           NOT NULL,
    id_profissional INT           NOT NULL,
    id_agendamento  INT           NULL,
    data_hora_inicio DATETIME     NOT NULL,
    data_hora_fim   DATETIME      NULL,
    anamnese        TEXT          NULL,
    prescricao      TEXT          NULL,
    observacoes     VARCHAR(500)  NULL,
    created_at      DATETIME      DEFAULT GETDATE(),
    CONSTRAINT FK_Atendimento_Paciente FOREIGN KEY (id_paciente)
        REFERENCES Paciente(id_paciente),
    CONSTRAINT FK_Atendimento_Profissional FOREIGN KEY (id_profissional)
        REFERENCES Profissional(id_profissional),
    CONSTRAINT FK_Atendimento_Agendamento FOREIGN KEY (id_agendamento)
        REFERENCES Agendamento(id_agendamento)
);

CREATE INDEX IX_Atendimento_Paciente ON Atendimento(id_paciente);
CREATE INDEX IX_Atendimento_Data ON Atendimento(data_hora_inicio);

-- =============================================================================
-- Tabela: Triagem
-- =============================================================================
CREATE TABLE Triagem (
    id_triagem       INT IDENTITY(1,1) PRIMARY KEY,
    id_atendimento   INT           NOT NULL,
    pressao_arterial VARCHAR(10)   NULL,
    temperatura      DECIMAL(4,1)  NULL,
    peso             DECIMAL(5,2)  NULL,
    altura           DECIMAL(3,2)  NULL,
    observacoes      VARCHAR(500)  NULL,
    created_at       DATETIME      DEFAULT GETDATE(),
    CONSTRAINT FK_Triagem_Atendimento FOREIGN KEY (id_atendimento)
        REFERENCES Atendimento(id_atendimento)
);

-- =============================================================================
-- Tabela: Fila
-- =============================================================================
CREATE TABLE Fila (
    id_fila         INT IDENTITY(1,1) PRIMARY KEY,
    id_paciente     INT           NOT NULL,
    id_consultorio  INT           NOT NULL,
    posicao         INT           NOT NULL,
    status          VARCHAR(20)   DEFAULT 'aguardando'
        CHECK (status IN ('aguardando', 'chamado', 'em_atendimento', 'atendido', 'desistiu')),
    hora_entrada    DATETIME      NOT NULL,
    hora_chamada    DATETIME      NULL,
    prioridade      INT           DEFAULT 0,
    created_at      DATETIME      DEFAULT GETDATE(),
    CONSTRAINT FK_Fila_Paciente FOREIGN KEY (id_paciente)
        REFERENCES Paciente(id_paciente),
    CONSTRAINT FK_Fila_Consultorio FOREIGN KEY (id_consultorio)
        REFERENCES Consultorio(id_consultorio)
);

CREATE INDEX IX_Fila_Consultorio_Status ON Fila(id_consultorio, status);
CREATE INDEX IX_Fila_Paciente ON Fila(id_paciente);
