# CAPÍTULO 3 — UX E UI DESIGN

## 3.1 Pesquisa Exploratória

A concepção da experiência de uso do sistema SaúdePOP partiu de uma pesquisa exploratória baseada em entrevistas fictícias e observação de cenários típicos de clínicas populares. A pesquisa identificou os principais pontos de dor de cada ator e orientou a criação de personas e jornadas.

### Principais Descobertas

- Recepcionistas alternam entre telefone, mensagens e balcão simultaneamente;
- Pacientes sentem ansiedade pela falta de informação sobre tempo de espera;
- Médicos perdem tempo buscando informações em prontuários de papel;
- A comunicação entre recepção e consultório é feita por deslocamento físico.

## 3.2 Personas

### Persona 1 — Maria dos Santos (Paciente)

| Atributo | Descrição |
|---|---|
| **Idade** | 58 anos |
| **Ocupação** | Dona de casa |
| **Escolaridade** | Ensino fundamental completo |
| **Contexto** | Frequenta a clínica mensalmente para acompanhamento de hipertensão |
| **Necessidades** | Saber quanto tempo vai esperar; não precisar repetir dados a cada consulta |
| **Frustrações** | Fila longa sem previsão; ter que explicar todo o histórico médico novamente |
| **Habilidade digital** | Baixa — usa celular apenas para WhatsApp e ligações |

### Persona 2 — Juliana Oliveira (Recepcionista)

| Atributo | Descrição |
|---|---|
| **Idade** | 32 anos |
| **Ocupação** | Recepcionista há 5 anos na clínica |
| **Escolaridade** | Ensino médio completo |
| **Contexto** | Responsável por cadastro, agendamento, cobrança e organização da fila |
| **Necessidades** | Cadastrar pacientes rapidamente; visualizar agenda do dia; organizar a fila sem sair do balcão |
| **Frustrações** | Lidar com conflitos de horário; não conseguir localizar prontuários; pacientes reclamando da espera |
| **Habilidade digital** | Média — usa computador diariamente para tarefas básicas |

### Persona 3 — Dr. Carlos Mendes (Profissional de Saúde)

| Atributo | Descrição |
|---|---|
| **Idade** | 45 anos |
| **Ocupação** | Médico clínico geral |
| **Escolaridade** | Ensino superior com especialização |
| **Contexto** | Atende 25-30 pacientes por dia em consultas de 15 minutos |
| **Necessidades** | Acessar histórico do paciente rapidamente; registrar atendimento de forma ágil; chamar próximo paciente sem depender da recepção |
| **Frustrações** | Prontuários ilegíveis; perda de tempo procurando informações; interrupções constantes |
| **Habilidade digital** | Alta — familiarizado com sistemas de saúde |

## 3.3 Mapas de Jornada do Usuário

### Jornada 1 — Paciente marca consulta e é atendido

| Etapa | Ação | Sentimento | Ponto de contato |
|---|---|---|---|
| 1. Agendamento | Liga para a clínica ou vai presencialmente | Ansiedade (será que tem vaga?) | Telefone / Balcão |
| 2. Chegada | Apresenta-se na recepção e confirma dados | Expectativa | Balcão da recepção |
| 3. Entrada na fila | Recebe senha e senta na sala de espera | Incerteza (quanto tempo?) | Sala de espera |
| 4. Acompanhamento | Olha o painel para ver sua posição | Alívio ao ver progresso | Painel de fila |
| 5. Chamada | Nome aparece no painel, é direcionado ao consultório | Satisfação | Painel / Recepção |
| 6. Atendimento | Consulta com o médico | Confiança | Consultório |
| 7. Saída | Recebe prescrição e próximo agendamento | Satisfação | Balcão |

### Jornada 2 — Recepcionista organiza o dia

| Etapa | Ação | Sentimento | Ponto de contato |
|---|---|---|---|
| 1. Abertura | Acessa o sistema e verifica agenda do dia | Organização | Sistema web |
| 2. Check-in | Confirma chegada dos pacientes agendados | Controle | Balcão / Sistema |
| 3. Gestão de fila | Adiciona pacientes à fila e monitora status | Concentração | Sistema web |
| 4. Encaixes | Insere pacientes sem agendamento na fila | Estresse | Sistema web |
| 5. Chamada | Aciona botão de chamar próximo paciente | Fluidez | Sistema web |
| 6. Fechamento | Verifica relatório de atendimentos do dia | Alívio | Sistema web |

## 3.4 Fluxo de Navegação

```
Login
  ├── Recepcionista
  │     ├── Dashboard (agenda do dia + fila)
  │     ├── Cadastro de Paciente
  │     ├── Agendamento de Consulta
  │     ├── Gestão de Fila
  │     │     ├── Adicionar à fila
  │     │     ├── Chamar próximo
  │     │     └── Visualizar painel
  │     └── Buscar Paciente
  │
  ├── Profissional de Saúde
  │     ├── Dashboard (fila do consultório)
  │     ├── Prontuário do Paciente
  │     │     ├── Histórico de atendimentos
  │     │     ├── Novo atendimento
  │     │     └── Triagem
  │     └── Chamar próximo paciente
  │
  ├── Administrador
  │     ├── Dashboard (indicadores)
  │     ├── Relatórios
  │     ├── Cadastro de Profissionais
  │     ├── Gestão de Consultórios
  │     └── Gestão de Usuários
  │
  └── Painel da Sala de Espera (sem login)
        └── Exibe fila em tempo real
```

## 3.5 Wireframes das Telas Principais

### Tela 1 — Login

```
┌──────────────────────────────────────────────┐
│              SAÚDE POP                       │
│         Sistema de Gestão Clínica            │
│                                              │
│     ┌──────────────────────────┐             │
│     │  Usuário                 │             │
│     └──────────────────────────┘             │
│     ┌──────────────────────────┐             │
│     │  Senha          ●●●●●●  │             │
│     └──────────────────────────┘             │
│                                              │
│     ┌──────────────────────────┐             │
│     │       ENTRAR             │             │
│     └──────────────────────────┘             │
│                                              │
│     Esqueceu a senha?                        │
└──────────────────────────────────────────────┘
```

### Tela 2 — Dashboard da Recepção

```
┌──────────────────────────────────────────────────────────┐
│ SAÚDE POP  │ Recepção │ Pacientes │ Agenda │ Fila │ Sair│
├──────────────────────────────────────────────────────────┤
│  AGENDA DO DIA                    │  FILA DE ESPERA     │
│  ┌────┬────────┬──────────┬────┐  │  Consultório 1      │
│  │ Hr │Paciente│Profission│ St │  │  ┌───┬────────┬───┐ │
│  ├────┼────────┼──────────┼────┤  │  │ # │ Nome   │ St│ │
│  │8:00│Maria S.│Dr.Carlos │ ✓  │  │  ├───┼────────┼───┤ │
│  │8:15│João P. │Dr.Carlos │ ◷  │  │  │ 1 │João P. │ ◷ │ │
│  │8:30│Ana L.  │Dra.Paula │ -  │  │  │ 2 │Ana L.  │ ● │ │
│  │8:45│Pedro R.│Dr.Carlos │ -  │  │  │ 3 │Pedro R.│ ● │ │
│  └────┴────────┴──────────┴────┘  │  └───┴────────┴───┘ │
│                                    │                     │
│  [+ Novo Agendamento]             │  [Chamar Próximo]   │
│                                    │  [+ Adicionar]      │
└──────────────────────────────────────────────────────────┘
```

### Tela 3 — Painel da Sala de Espera

```
┌──────────────────────────────────────────────────────────┐
│                    SAÚDE POP                             │
│              Painel de Chamada                           │
│                                                          │
│  ┌──────────────────────────────────────────────┐        │
│  │  CHAMANDO:  MARIA DOS SANTOS                 │        │
│  │  Consultório 2 — Dr. Carlos Mendes            │        │
│  └──────────────────────────────────────────────┘        │
│                                                          │
│  Próximos:                                               │
│  ┌───┬──────────────────┬─────────────────┐              │
│  │ 1 │ João P. Silva    │ Consultório 1   │              │
│  │ 2 │ Ana L. Costa     │ Consultório 2   │              │
│  │ 3 │ Pedro R. Santos  │ Consultório 1   │              │
│  └───┴──────────────────┴─────────────────┘              │
│                                                          │
│  Hora atual: 08:22    Tempo médio de espera: 12 min      │
└──────────────────────────────────────────────────────────┘
```

### Tela 4 — Prontuário do Paciente (Visão do Médico)

```
┌──────────────────────────────────────────────────────────┐
│ SAÚDE POP │ Meu Consultório │ Prontuários │ Fila │ Sair │
├──────────────────────────────────────────────────────────┤
│  PACIENTE: Maria dos Santos    CPF: 123.456.789-01      │
│  Idade: 58 anos    Tel: (11) 99999-0000                  │
├──────────────────────────────────────────────────────────┤
│  TRIAGEM          │  HISTÓRICO DE ATENDIMENTOS           │
│  PA: 140/90 mmHg  │  ┌──────────┬──────────┬──────────┐ │
│  Temp: 36.5°C     │  │  Data    │ Médico   │ Resumo   │ │
│  Peso: 72 kg      │  ├──────────┼──────────┼──────────┤ │
│  Altura: 1.60 m   │  │15/02/25 │Dr.Carlos │Controle  │ │
│                    │  │18/01/25 │Dr.Carlos │Retorno   │ │
│  NOVO ATENDIMENTO │  │10/12/24 │Dra.Paula │Exames    │ │
│  ┌──────────────┐ │  └──────────┴──────────┴──────────┘ │
│  │ Anamnese:    │ │                                      │
│  │              │ │                                      │
│  │ Prescrição:  │ │                                      │
│  │              │ │                                      │
│  │ [Salvar]     │ │                                      │
│  └──────────────┘ │                                      │
└──────────────────────────────────────────────────────────┘
```

## 3.6 Princípios de Design Aplicados

- **Hierarquia visual**: informações mais importantes (fila, chamada) com maior destaque;
- **Tipografia**: fonte sans-serif (Inter/Roboto) para leitura rápida; tamanhos diferenciados para títulos e corpo;
- **Contraste**: fundo claro com texto escuro; botões de ação em cores primárias (azul para ações, verde para confirmação, vermelho para cancelamento);
- **Acessibilidade**: contraste mínimo WCAG AA (4.5:1); botões com tamanho mínimo de 44px; textos legíveis em tamanho 16px+;
- **Consistência**: mesmos padrões de navegação, cores e ícones em todas as telas.

## 3.7 Teste de Usabilidade

### Metodologia

Foi conduzido um ciclo de teste de usabilidade com 3 colegas atuando como usuários simulados, representando cada persona. Cada participante recebeu 4 tarefas para executar no protótipo.

### Tarefas e Resultados

| Tarefa | Persona | Tempo Médio | Taxa de Sucesso | Dificuldades |
|---|---|---|---|---|
| Cadastrar um paciente | Recepcionista | 2 min | 100% | Nenhuma |
| Adicionar paciente à fila | Recepcionista | 1 min | 100% | Botão pouco visível inicialmente |
| Verificar posição na fila | Paciente | 30 seg | 100% | Nenhuma |
| Registrar atendimento | Médico | 3 min | 67% | Campo de prescrição confuso |

### Melhorias Aplicadas

Com base nos testes, as seguintes melhorias foram implementadas:

1. **Botão "Adicionar à Fila"** foi destacado com cor verde e ícone de "+" para melhor visibilidade;
2. **Campo de prescrição** foi separado em subcampos (medicamento, dosagem, frequência) para facilitar o preenchimento;
3. **Painel da sala de espera** recebeu fonte maior (32px) para leitura à distância;
4. **Feedback visual** foi adicionado ao confirmar ações (toast de sucesso/erro).
