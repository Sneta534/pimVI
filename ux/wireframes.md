# Wireframes — SaúdePOP

## Descrição

Os wireframes a seguir representam as telas principais do sistema SaúdePOP em baixa fidelidade. O protótipo navegável foi desenvolvido em Figma e está representado aqui por meio de descrições textuais e diagramas ASCII.

---

## Tela 1: Login

```
┌──────────────────────────────────────────────────┐
│                                                  │
│              ┌──────────────────┐                │
│              │   SAÚDE POP      │                │
│              │   🏥              │                │
│              └──────────────────┘                │
│         Sistema de Gestão Clínica                │
│                                                  │
│         ┌─────────────────────────┐              │
│         │  👤 Usuário              │              │
│         └─────────────────────────┘              │
│         ┌─────────────────────────┐              │
│         │  🔒 Senha    ●●●●●●●    │              │
│         └─────────────────────────┘              │
│                                                  │
│         ┌─────────────────────────┐              │
│         │      [ ENTRAR ]         │              │
│         └─────────────────────────┘              │
│                                                  │
│         Esqueceu a senha?                        │
│                                                  │
└──────────────────────────────────────────────────┘
```

**Elementos**: Campo de usuário, campo de senha (mascarado), botão "Entrar", link "Esqueceu a senha?".
**Ação principal**: Autenticar usuário e redirecionar ao dashboard do perfil correspondente.

---

## Tela 2: Dashboard da Recepção

```
┌──────────────────────────────────────────────────────────────┐
│ 🏥 SAÚDE POP │ Recepção │ Pacientes │ Agenda │ Fila │ [Sair]│
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  📅 AGENDA DO DIA - 15/03/2025          📊 FILA DE ESPERA   │
│  ┌──────┬──────────────┬────────────┬───────┐  Consultório 1 │
│  │ Hora │ Paciente     │ Médico     │Status │  ┌──┬─────────┐│
│  ├──────┼──────────────┼────────────┼───────┤  │# │ Nome    ││
│  │ 8:00 │ Maria Santos │ Dr.Carlos  │  ✅   │  ├──┼─────────┤│
│  │ 8:15 │ João Silva   │ Dr.Carlos  │  ⏳   │  │1 │João S.  ││
│  │ 8:30 │ Ana Costa    │ Dra.Paula  │  —    │  │2 │Ana C.   ││
│  │ 8:45 │ Pedro R.     │ Dr.Carlos  │  —    │  │3 │Pedro R. ││
│  │ 9:00 │ Francisca O. │ Dr.Carlos  │  —    │  └──┴─────────┘│
│  └──────┴──────────────┴────────────┴───────┘                │
│                                              [Chamar Próximo]│
│  [+ Novo Agendamento]  [🔍 Buscar Paciente] [+ Add à Fila]  │
│                                                              │
│  Resumo: 28 agendados │ 5 atendidos │ 2 faltas │ 21 restam  │
└──────────────────────────────────────────────────────────────┘
```

**Elementos**: Menu superior com navegação por perfil; tabela de agenda do dia; painel lateral de fila; botões de ação rápida; resumo estatístico do dia.
**Ação principal**: Visão consolidada do dia com acesso rápido às operações principais.

---

## Tela 3: Cadastro de Paciente

```
┌──────────────────────────────────────────────────────────────┐
│ 🏥 SAÚDE POP │ Recepção │ Pacientes │ Agenda │ Fila │ [Sair]│
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  📋 CADASTRO DE PACIENTE                                     │
│                                                              │
│  Nome completo *    ┌──────────────────────────────────┐     │
│                     │                                  │     │
│                     └──────────────────────────────────┘     │
│  CPF *              ┌────────────────┐                       │
│                     │                │                       │
│                     └────────────────┘                       │
│  Data de nascimento * ┌──────────┐   Sexo  ○ M  ○ F         │
│                       │ dd/mm/aa │                           │
│                       └──────────┘                           │
│  Telefone           ┌────────────────┐                       │
│                     │                │                       │
│                     └────────────────┘                       │
│  E-mail             ┌──────────────────────────────────┐     │
│                     │                                  │     │
│                     └──────────────────────────────────┘     │
│  Endereço           ┌──────────────────────────────────┐     │
│                     │                                  │     │
│                     └──────────────────────────────────┘     │
│                                                              │
│                     [ Cancelar ]     [ Salvar ]               │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Elementos**: Formulário com campos obrigatórios (*) e opcionais; validação de CPF em tempo real; botões "Cancelar" e "Salvar".
**Ação principal**: Cadastrar novo paciente no sistema.

---

## Tela 4: Painel da Sala de Espera

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│                      🏥 SAÚDE POP                            │
│                  Painel de Chamada                            │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │                                                      │    │
│  │   🔔  CHAMANDO:                                      │    │
│  │                                                      │    │
│  │       MARIA DOS SANTOS                               │    │
│  │       Consultório 2 — Dr. Carlos Mendes              │    │
│  │                                                      │    │
│  └──────────────────────────────────────────────────────┘    │
│                                                              │
│  Próximos na fila:                                           │
│  ┌────┬──────────────────────┬──────────────────┐            │
│  │  1 │ João Pedro Silva     │ Consultório 1    │            │
│  │  2 │ Ana Luíza Costa      │ Consultório 2    │            │
│  │  3 │ Pedro Rodrigues      │ Consultório 1    │            │
│  │  4 │ Francisca Oliveira   │ Consultório 3    │            │
│  └────┴──────────────────────┴──────────────────┘            │
│                                                              │
│  🕐 Hora: 08:22        ⏱️  Tempo médio de espera: 12 min    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Elementos**: Nome do paciente chamado em destaque; lista dos próximos; hora atual; tempo médio de espera.
**Ação principal**: Exibir informações da fila para pacientes na sala de espera (tela sem interação, modo TV/monitor).

---

## Tela 5: Prontuário do Paciente (Visão do Médico)

```
┌──────────────────────────────────────────────────────────────┐
│ 🏥 SAÚDE POP │ Consultório │ Prontuários │ Minha Fila │[Sair]│
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  👤 PACIENTE: Maria dos Santos       CPF: 123.456.789-01    │
│     Idade: 58 anos   Telefone: (11) 99999-0000              │
│  ─────────────────────────────────────────────────────────── │
│                                                              │
│  🩺 TRIAGEM                │  📋 HISTÓRICO                  │
│  ┌──────────────────────┐  │  ┌──────────┬────────┬───────┐ │
│  │ PA:   140/90 mmHg    │  │  │ Data     │ Médico │Resumo │ │
│  │ Temp: 36.5 °C        │  │  ├──────────┼────────┼───────┤ │
│  │ Peso: 72 kg          │  │  │ 15/02/25 │Dr.Carl.│Contro.│ │
│  │ Alt:  1.60 m         │  │  │ 18/01/25 │Dr.Carl.│Retorn.│ │
│  │ IMC:  28.1           │  │  │ 10/12/24 │Dra.Pau.│Exames │ │
│  └──────────────────────┘  │  │ 15/11/24 │Dr.Carl.│Contro.│ │
│                             │  └──────────┴────────┴───────┘ │
│  📝 NOVO ATENDIMENTO       │                                 │
│  ┌──────────────────────┐  │  [Ver atendimento completo]     │
│  │ Anamnese:            │  │                                 │
│  │ ____________________│  │                                 │
│  │ ____________________│  │                                 │
│  │                      │  │                                 │
│  │ Prescrição:          │  │                                 │
│  │ Medicamento: _______ │  │                                 │
│  │ Dosagem: ___________│  │                                 │
│  │ Frequência: ________│  │                                 │
│  │ [+ Add medicamento]  │  │                                 │
│  │                      │  │                                 │
│  │ Observações:         │  │                                 │
│  │ ____________________│  │                                 │
│  └──────────────────────┘  │                                 │
│                             │                                 │
│  [ Salvar Atendimento ]     │  [ Chamar Próximo Paciente ]   │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**Elementos**: Dados do paciente no topo; dados da triagem à esquerda; histórico à direita; formulário de atendimento estruturado com campos separados para medicamento, dosagem e frequência; botões de ação.
**Ação principal**: Registrar atendimento e acessar histórico clínico do paciente.

---

## Princípios de Design Aplicados

| Princípio | Aplicação |
|---|---|
| **Hierarquia visual** | Informações críticas (chamada, fila) com maior destaque e fonte |
| **Consistência** | Mesmo layout de navegação, cores e ícones em todas as telas |
| **Feedback** | Toast de confirmação para todas as ações (salvar, excluir, chamar) |
| **Eficiência** | Ações frequentes acessíveis com 1-2 cliques |
| **Acessibilidade** | Contraste WCAG AA, botões ≥44px, fonte ≥16px |
| **Legibilidade à distância** | Painel de sala de espera com fonte ≥32px |
