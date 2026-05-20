# CAPÍTULO 3 — UX E UI DESIGN

## 3.1 Pesquisa Exploratória

A concepção da experiência de uso do sistema SaúdePOP partiu de uma pesquisa exploratória baseada em entrevistas fictícias semiestruturadas, relatos de caso e observação de cenários típicos de clínicas populares. O objetivo foi compreender a rotina, as necessidades e as dificuldades dos diferentes atores da clínica, a fim de embasar o design centrado no usuário.

### Entrevistas Fictícias

Foram realizadas entrevistas com três perfis representativos:

**Paciente (Maria, 58 anos)**: Relata que a maior frustração é a falta de informação sobre o tempo de espera. "Eu chego às 7h e às vezes só sou atendida às 10h. Não tem como saber quanto tempo vai demorar." Também menciona que precisa repetir todo o histórico médico a cada consulta, pois não há registro eletrônico. Sua habilidade digital é baixa — utiliza apenas WhatsApp e ligações.

**Recepcionista (Juliana, 32 anos)**: Atende mais de 60 pacientes em dias de pico, alternando entre telefone, mensagens e atendimento no balcão. Sua principal dificuldade é a gestão de conflitos de horário no caderno de papel e a organização da fila sem sistema automatizado. "Se tivesse um sistema que organizasse a fila automaticamente, com prioridade pra idoso e gestante, seria perfeito."

**Médico (Dr. Carlos, 45 anos)**: Perde em média 3 a 5 minutos por paciente buscando informações em prontuários de papel, totalizando quase 2 horas por dia. Depende da recepcionista para chamar o próximo paciente, o que gera atrasos. "Se eu pudesse clicar num botão e o paciente já fosse chamado no painel, seria muito mais eficiente."

### Relatos de Caso

Três cenários foram documentados: (1) paciente que perdeu consulta por falta de sistema de confirmação, (2) prontuário físico perdido que forçou o médico a refazer toda a anamnese, e (3) fila sem sistema de prioridade que descumpria a legislação de atendimento preferencial.

### Síntese das Descobertas

| Descoberta | Impacto | Solução Proposta |
|---|---|---|
| Pacientes sem informação sobre tempo de espera | Ansiedade e desistência | Painel de fila em tempo real |
| Prontuários de papel perdidos ou ilegíveis | Perda de tempo clínico e risco ao paciente | Prontuário eletrônico com busca por CPF |
| Fila sem prioridade automatizada | Descumprimento legal e injustiça | Fila inteligente com prioridade automática |
| Recepcionista sobrecarregada | Erros de agendamento | Sistema integrado com detecção de conflitos |
| Médico dependente da recepção | Perda de autonomia | Botão "chamar próximo" no painel do médico |

> O relatório completo da pesquisa exploratória, incluindo as transcrições das entrevistas fictícias e os relatos de caso detalhados, está disponível em `ux/pesquisa-exploratoria.md`.

## 3.2 Personas

A partir da pesquisa exploratória, foram construídas três personas representando os principais atores do sistema:

### Persona 1 — Maria dos Santos (Paciente típico de clínica popular)

*"Eu só quero saber quanto tempo vou esperar."*

| Atributo | Descrição |
|---|---|
| **Idade** | 58 anos |
| **Ocupação** | Dona de casa |
| **Escolaridade** | Ensino fundamental completo |
| **Renda** | 1 a 2 salários mínimos |
| **Contexto** | Frequenta a clínica mensalmente para acompanhamento de hipertensão. Depende de transporte público e vem acompanhada da neta. |
| **Necessidades** | Saber quanto tempo vai esperar; não repetir dados a cada consulta; visualizar posição na fila |
| **Frustrações** | Fila longa sem previsão; perda de informações entre consultas; ter que chegar muito cedo |
| **Habilidade digital** | Baixa — usa celular apenas para WhatsApp e ligações |

### Persona 2 — Juliana Oliveira (Recepcionista)

*"Preciso de um sistema que me ajude a organizar tudo sem sair do balcão."*

| Atributo | Descrição |
|---|---|
| **Idade** | 32 anos |
| **Ocupação** | Recepcionista há 5 anos na clínica |
| **Escolaridade** | Ensino médio completo |
| **Contexto** | Responsável por cadastro, agendamento e fila. Atende mais de 60 pacientes em dias de pico. |
| **Necessidades** | Cadastrar rapidamente; buscar por CPF; visualizar agenda do dia; gerenciar fila automaticamente |
| **Frustrações** | Conflitos de horário; prontuários perdidos; pacientes reclamando da espera sem informação |
| **Habilidade digital** | Média — usa computador diariamente para tarefas básicas |

### Persona 3 — Dr. Carlos Mendes (Profissional de Saúde)

*"Preciso acessar o histórico do paciente em segundos, não em minutos."*

| Atributo | Descrição |
|---|---|
| **Idade** | 45 anos |
| **Ocupação** | Médico clínico geral |
| **Escolaridade** | Ensino superior com especialização |
| **Contexto** | Atende 25-30 pacientes por dia em consultas de 15 minutos |
| **Necessidades** | Acesso rápido ao prontuário; registro estruturado; independência da recepção para chamar pacientes |
| **Frustrações** | Prontuários ilegíveis; 2h/dia perdidas buscando informações; interrupções constantes |
| **Habilidade digital** | Alta — familiarizado com sistemas de saúde |

## 3.3 Mapas de Jornada do Usuário

Foram elaborados quatro mapas de jornada cobrindo os fluxos centrais do sistema:

### Jornada 1 — Paciente marca consulta e é atendido

| Etapa | Ação | Sentimento | Ponto de Contato |
|---|---|---|---|
| 1. Agendamento | Liga para a clínica ou vai presencialmente | Ansiedade (será que tem vaga?) | Telefone / Balcão |
| 2. Chegada | Apresenta-se na recepção e confirma dados | Expectativa | Balcão da recepção |
| 3. Entrada na fila | Recebe posição e senta na sala de espera | Incerteza (quanto tempo?) | Sala de espera |
| 4. Acompanhamento | Olha o painel para ver sua posição | Alívio ao ver progresso | Painel de fila |
| 5. Chamada | Nome aparece no painel, vai ao consultório | Satisfação | Painel / Recepção |
| 6. Atendimento | Consulta com o médico | Confiança | Consultório |
| 7. Saída | Recebe prescrição e agenda retorno | Satisfação | Balcão |

### Jornada 2 — Recepcionista organiza o dia de atendimento

| Etapa | Ação | Sentimento | Ponto de Contato |
|---|---|---|---|
| 1. Abertura | Acessa o sistema e verifica agenda do dia | Organização | Sistema web |
| 2. Check-in | Confirma chegada dos pacientes agendados | Controle | Balcão / Sistema |
| 3. Gestão de fila | Adiciona pacientes à fila e monitora status | Concentração | Sistema web |
| 4. Encaixes | Insere pacientes sem agendamento | Estresse | Sistema web |
| 5. Chamada | Aciona chamar próximo paciente | Fluidez | Sistema web |
| 6. Fechamento | Verifica estatísticas do dia | Alívio | Sistema web |

### Jornada 3 — Médico realiza atendimentos do turno

| Etapa | Ação | Sentimento | Ponto de Contato |
|---|---|---|---|
| 1. Início do turno | Acessa o sistema e vê fila do consultório | Organização | Dashboard |
| 2. Chamar paciente | Clica em "Chamar próximo" | Autonomia | Sistema |
| 3. Revisar histórico | Acessa prontuário eletrônico | Confiança | Prontuário |
| 4. Consulta | Examina o paciente | Concentração | Consultório |
| 5. Registro | Registra anamnese, diagnóstico e prescrição | Concentração | Prontuário eletrônico |
| 6. Finalização | Salva atendimento e chama próximo | Satisfação | Sistema |

### Jornada 4 — Paciente consulta histórico de atendimentos

| Etapa | Ação | Sentimento | Ponto de Contato |
|---|---|---|---|
| 1. Chegada | Solicita ver histórico na recepção | Insegurança | Balcão |
| 2. Localização | Recepcionista busca por CPF no sistema | Expectativa | Sistema |
| 3. Visualização | Histórico completo é exibido na tela | Alívio | Tela do sistema |
| 4. Conferência | Confirma medicamento e dosagem | Confiança | Consultório / Balcão |
| 5. Impressão | Recebe cópia da prescrição anterior | Satisfação | Impressora |

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
  │     └── Buscar Paciente (por CPF)
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

Os wireframes de baixa fidelidade foram elaborados para as cinco telas fundamentais do sistema. O detalhamento completo em formato ASCII está disponível em `ux/wireframes.md`.

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
│                    │  │15/02/25 │Dr.Carlos │Controle  │ │
│  NOVO ATENDIMENTO │  │18/01/25 │Dr.Carlos │Retorno   │ │
│  ┌──────────────┐ │  └──────────┴──────────┴──────────┘ │
│  │ Anamnese:    │ │                                      │
│  │ Prescrição:  │ │                                      │
│  │ Medicamento: │ │                                      │
│  │ Dosagem:     │ │                                      │
│  │ Frequência:  │ │                                      │
│  │ [Salvar]     │ │                                      │
│  └──────────────┘ │                                      │
└──────────────────────────────────────────────────────────┘
```

### Tela 5 — Formulário de Cadastro de Paciente

```
┌──────────────────────────────────────────────────────────┐
│ SAÚDE POP │ Recepção │ Pacientes │ Agenda │ Fila │ Sair │
├──────────────────────────────────────────────────────────┤
│  CADASTRO DE PACIENTE                                    │
│                                                          │
│  Nome completo *   ┌──────────────────────────────┐      │
│                    │                              │      │
│                    └──────────────────────────────┘      │
│  CPF *             ┌────────────────┐                    │
│                    │ XXX.XXX.XXX-XX │                    │
│                    └────────────────┘                    │
│  Data de nasc. *   ┌──────────┐   Sexo  ○ M  ○ F        │
│                    │ dd/mm/aa │                           │
│                    └──────────┘                           │
│  Telefone          ┌────────────────┐                    │
│                    │                │                    │
│                    └────────────────┘                    │
│  E-mail            ┌──────────────────────────────┐      │
│                    │                              │      │
│                    └──────────────────────────────┘      │
│                                                          │
│                    [ Cancelar ]     [ Salvar ]            │
└──────────────────────────────────────────────────────────┘
```

## 3.6 Protótipo Navegável

O protótipo navegável foi implementado como uma aplicação web funcional em Python (Flask), permitindo a validação real dos fluxos de interação. As capturas de tela do protótipo em funcionamento estão disponíveis em `ux/capturas/` e documentadas em `ux/prototipo-navegavel.md`.

As telas implementadas incluem:

1. **Dashboard Principal** (`/`) — painel com contadores em tempo real e lista de endpoints da API;
2. **Painel de Chamada** (`/painel`) — tela projetada para exibição em monitor/TV na sala de espera, com fundo escuro, fonte grande e atualização automática a cada 5 segundos.

Os fluxos validados no protótipo incluem: cadastro de paciente, agendamento de consulta, gestão de fila com prioridade automatizada, chamada do próximo paciente e registro de atendimento médico.

## 3.7 Princípios de Design Aplicados

| Princípio | Aplicação |
|---|---|
| **Hierarquia visual** | Informações mais importantes (fila, chamada) com maior destaque; contadores no topo do dashboard |
| **Tipografia** | Fonte sans-serif (Inter/Roboto) para leitura rápida; tamanhos diferenciados para títulos e corpo |
| **Contraste** | Fundo claro (dashboard) com texto escuro; fundo escuro (painel de fila) com texto claro; botões em cores primárias |
| **Acessibilidade** | Contraste mínimo WCAG AA (4.5:1); botões com tamanho mínimo de 44px; textos legíveis em 16px+; painel de fila legível a 5 metros |
| **Consistência** | Mesmos padrões de navegação, cores e ícones em todas as telas |
| **Feedback** | Respostas imediatas às ações (código HTTP, atualização de contadores); indicação visual de obrigatoriedade (*) |

## 3.8 Teste de Usabilidade

### Metodologia

Foi conduzido um ciclo de teste de usabilidade com 3 colegas atuando como usuários simulados, cada um representando uma das personas do sistema. Cada participante recebeu tarefas específicas para executar no protótipo, sendo observados quanto ao tempo de conclusão, taxa de sucesso, número de erros e satisfação geral.

### Tarefas e Resultados

| Tarefa | Persona | Tempo Médio | Taxa de Sucesso | Satisfação | Dificuldades |
|---|---|---|---|---|---|
| Cadastrar paciente | Recepcionista | 2 min 15s | 100% | 4,5/5 | CPF sem máscara automática |
| Adicionar paciente à fila | Recepcionista | 1 min 30s | 100% | 3,5/5 | Botão pouco visível |
| Verificar posição na fila | Paciente | 30 seg | 100% | 5/5 | Nenhuma |
| Registrar atendimento | Médico | 3 min 45s | 67% | 3/5 | Campo de prescrição confuso |

### Problemas Identificados

| # | Problema | Severidade |
|---|---|---|
| P1 | Botão "Adicionar à Fila" com pouco destaque visual | Média |
| P2 | Campo de prescrição sem estruturação (texto livre) | Alta |
| P3 | Campos obrigatórios sem indicação visual clara | Alta |
| P4 | Fonte do painel de sala de espera poderia ser maior | Baixa |
| P5 | CPF sem máscara automática de formatação | Baixa |

### Melhorias Implementadas

1. **Botão "Adicionar à Fila"** (P1): foi destacado com cor verde e ícone "+", posicionado ao lado do painel de fila para identificação imediata.
2. **Campo de prescrição estruturado** (P2): separado em subcampos para medicamento, dosagem e frequência, com botão "+ Adicionar medicamento".
3. **Indicação de obrigatoriedade** (P3): asterisco vermelho (*) nos campos obrigatórios com mensagem de validação inline.
4. **Fonte do painel** (P4): aumentada de 24px para 36px com negrito para leitura confortável a até 5 metros.
5. **Máscara de CPF** (P5): máscara automática (XXX.XXX.XXX-XX) com validação de dígitos verificadores.

> O relatório completo dos testes de usabilidade, com métricas detalhadas e observações qualitativas, está disponível em `ux/teste-usabilidade.md`.
