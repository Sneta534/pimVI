# Diagrama Entidade-Relacionamento — SaúdePOP

## Visão Geral

O diagrama ER do sistema SaúdePOP contempla 8 entidades principais que sustentam as operações de prontuário eletrônico, agendamento e fila inteligente.

## Diagrama

```
┌───────────────┐          ┌──────────────────┐          ┌──────────────────┐
│   PACIENTE    │          │   AGENDAMENTO    │          │  PROFISSIONAL    │
├───────────────┤          ├──────────────────┤          ├──────────────────┤
│ PK id_paciente│──┐       │ PK id_agendamento│      ┌──│ PK id_profission │
│    nome       │  │  1:N  │ FK id_paciente   │──────┘  │    nome          │
│    cpf (UQ)   │  └──────>│ FK id_profission │  N:1    │    crm (UQ)      │
│    data_nasc  │          │ FK id_consultorio│──┐      │    especialidade  │
│    telefone   │          │    data_hora     │  │      │    telefone       │
│    email      │          │    status        │  │      │    email          │
│    endereco   │          │    observacoes   │  │      │    ativo          │
│    created_at │          │    created_at    │  │      │    created_at     │
└───────────────┘          └──────────────────┘  │      └──────────────────┘
       │                          │              │             │
       │                     1:1  │              │             │
       │                          ▼              │             │
       │                   ┌──────────────┐      │      ┌──────────────┐
       │              1:N  │ ATENDIMENTO  │      │      │   USUARIO    │
       └──────────────────>├──────────────┤      │      ├──────────────┤
                           │ PK id_atend  │      │      │ PK id_usuario│
                           │ FK id_pacien │      │      │    login (UQ)│
                           │ FK id_profis │      │      │    senha_hash│
                           │ FK id_agenda │      │      │    perfil    │
                           │ data_hr_ini  │      │      │ FK id_profis │
                           │ data_hr_fim  │      │      │    ativo     │
                           │ anamnese     │      │      │    created_at│
                           │ prescricao   │      │      └──────────────┘
                           │ observacoes  │      │
                           │ created_at   │      │
                           └──────────────┘      │
                                  │              │
                             1:1  │              │
                                  ▼              │
                           ┌──────────────┐      │      ┌──────────────────┐
                           │   TRIAGEM    │      │      │  CONSULTORIO     │
                           ├──────────────┤      │      ├──────────────────┤
                           │ PK id_triagem│      └─────>│ PK id_consultorio│
                           │ FK id_atend  │        N:1  │    numero (UQ)   │
                           │ pressao_art  │             │    andar         │
                           │ temperatura  │             │    especialidade │
                           │ peso         │             │    ativo         │
                           │ altura       │             └──────────────────┘
                           │ observacoes  │                    │
                           │ created_at   │                    │
                           └──────────────┘                    │
                                                          1:N  │
       ┌───────────────────────────────────────────────────────┘
       │
       ▼
┌──────────────────┐
│      FILA        │
├──────────────────┤
│ PK id_fila       │
│ FK id_paciente   │<── PACIENTE (1:N)
│ FK id_consultorio│
│    posicao       │
│    status        │
│    hora_entrada  │
│    hora_chamada  │
│    prioridade    │
│    created_at    │
└──────────────────┘
```

## Cardinalidades

| Relacionamento | Cardinalidade | Descrição |
|---|---|---|
| PACIENTE → AGENDAMENTO | 1:N | Um paciente pode ter vários agendamentos |
| PROFISSIONAL → AGENDAMENTO | 1:N | Um profissional atende vários agendamentos |
| CONSULTORIO → AGENDAMENTO | 1:N | Cada agendamento ocorre em um consultório |
| AGENDAMENTO → ATENDIMENTO | 1:1 | Cada agendamento pode gerar um atendimento |
| PACIENTE → ATENDIMENTO | 1:N | Um paciente pode ter vários atendimentos |
| PROFISSIONAL → ATENDIMENTO | 1:N | Um profissional realiza vários atendimentos |
| ATENDIMENTO → TRIAGEM | 1:1 | Cada atendimento pode ter uma triagem |
| PACIENTE → FILA | 1:N | Um paciente pode entrar na fila várias vezes |
| CONSULTORIO → FILA | 1:N | A fila é organizada por consultório |
| PROFISSIONAL → USUARIO | 1:1 | Um profissional pode ter um usuário associado |
