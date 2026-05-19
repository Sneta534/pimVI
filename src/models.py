"""
SaúdePOP — Modelos de Dados
Representação das entidades do sistema em Python.
"""

from dataclasses import dataclass, field
from datetime import date, datetime


@dataclass
class Paciente:
    id_paciente: int
    nome: str
    cpf: str
    data_nascimento: date
    telefone: str = ""
    email: str = ""
    endereco: str = ""
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def idade(self) -> int:
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - (
            (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)
        )

    @property
    def cpf_formatado(self) -> str:
        c = self.cpf
        return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"


@dataclass
class Profissional:
    id_profissional: int
    nome: str
    crm: str
    especialidade: str
    telefone: str = ""
    email: str = ""
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Consultorio:
    id_consultorio: int
    numero: int
    andar: int = 1
    especialidade: str = ""
    ativo: bool = True


@dataclass
class Agendamento:
    id_agendamento: int
    id_paciente: int
    id_profissional: int
    id_consultorio: int
    data_hora: datetime
    status: str = "agendado"
    observacoes: str = ""
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Atendimento:
    id_atendimento: int
    id_paciente: int
    id_profissional: int
    data_hora_inicio: datetime
    id_agendamento: int = 0
    data_hora_fim: datetime = None
    anamnese: str = ""
    prescricao: str = ""
    observacoes: str = ""
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Triagem:
    id_triagem: int
    id_atendimento: int
    pressao_arterial: str = ""
    temperatura: float = 0.0
    peso: float = 0.0
    altura: float = 0.0
    observacoes: str = ""
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def imc(self) -> float:
        if self.altura > 0:
            return round(self.peso / (self.altura ** 2), 1)
        return 0.0


@dataclass
class FilaEspera:
    id_fila: int
    id_paciente: int
    id_consultorio: int
    posicao: int
    status: str = "aguardando"
    hora_entrada: datetime = field(default_factory=datetime.now)
    hora_chamada: datetime = None
    prioridade: int = 0
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class Usuario:
    id_usuario: int
    login: str
    senha_hash: str
    perfil: str
    id_profissional: int = 0
    ativo: bool = True
    created_at: datetime = field(default_factory=datetime.now)
