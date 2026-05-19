# Relatório de Teste de Usabilidade — SaúdePOP

## 1. Metodologia

### Objetivo
Avaliar a usabilidade do protótipo do sistema SaúdePOP com usuários simulados, identificando dificuldades de uso e oportunidades de melhoria.

### Participantes
Foram selecionados 3 colegas para atuar como usuários simulados, cada um representando uma das personas do sistema:

| Participante | Persona Representada | Perfil |
|---|---|---|
| Participante A | Maria (Paciente) | Pouca experiência com computadores |
| Participante B | Juliana (Recepcionista) | Experiência média com computadores |
| Participante C | Dr. Carlos (Médico) | Alta experiência com sistemas |

### Tarefas Avaliadas

| # | Tarefa | Persona | Tela Avaliada |
|---|---|---|---|
| T1 | Cadastrar um novo paciente | Recepcionista | Cadastro de Paciente |
| T2 | Adicionar um paciente à fila de espera | Recepcionista | Dashboard da Recepção |
| T3 | Verificar posição na fila | Paciente | Painel da Sala de Espera |
| T4 | Registrar um atendimento no prontuário | Médico | Prontuário do Paciente |

### Métricas Coletadas
- Tempo para conclusão da tarefa
- Taxa de sucesso (conseguiu/não conseguiu)
- Número de erros ou cliques extras
- Nível de satisfação (1 a 5)
- Observações qualitativas

## 2. Resultados

### Tarefa 1: Cadastrar um novo paciente

| Métrica | Resultado |
|---|---|
| Tempo médio | 2 min 15 seg |
| Taxa de sucesso | 100% |
| Erros | 0 |
| Satisfação | 4,5 / 5 |

**Observações**: O fluxo foi considerado intuitivo. O participante sugeriu que o campo CPF tivesse máscara automática de formatação.

### Tarefa 2: Adicionar paciente à fila de espera

| Métrica | Resultado |
|---|---|
| Tempo médio | 1 min 30 seg |
| Taxa de sucesso | 100% |
| Erros | 1 (clicou no local errado inicialmente) |
| Satisfação | 3,5 / 5 |

**Observações**: O botão "Adicionar à Fila" estava com pouco destaque visual. O participante não o identificou de imediato e procurou a funcionalidade no menu superior antes de encontrá-lo.

### Tarefa 3: Verificar posição na fila

| Métrica | Resultado |
|---|---|
| Tempo médio | 30 seg |
| Taxa de sucesso | 100% |
| Erros | 0 |
| Satisfação | 5 / 5 |

**Observações**: O painel da sala de espera foi considerado claro e fácil de ler. O participante sugeriu que a fonte poderia ser ainda maior para pessoas com dificuldade visual.

### Tarefa 4: Registrar atendimento no prontuário

| Métrica | Resultado |
|---|---|
| Tempo médio | 3 min 45 seg |
| Taxa de sucesso | 67% (1 de 3 não completou) |
| Erros | 2 |
| Satisfação | 3 / 5 |

**Observações**: O campo de prescrição em formato livre causou confusão. O participante não sabia se deveria escrever o medicamento, dosagem e frequência tudo junto ou separado. Um participante não conseguiu salvar o atendimento por não ter preenchido o campo obrigatório de anamnese (faltou indicação visual de obrigatoriedade).

## 3. Problemas Identificados

| # | Problema | Severidade | Tarefa |
|---|---|---|---|
| P1 | Botão "Adicionar à Fila" com pouco destaque visual | Média | T2 |
| P2 | Campo de prescrição sem estruturação | Alta | T4 |
| P3 | Campos obrigatórios sem indicação visual clara | Alta | T4 |
| P4 | Fonte do painel de sala de espera poderia ser maior | Baixa | T3 |
| P5 | CPF sem máscara automática de formatação | Baixa | T1 |

## 4. Melhorias Implementadas

Com base nos testes, as seguintes melhorias foram aplicadas ao protótipo:

### Melhoria 1 — Botão "Adicionar à Fila" (P1)
- **Antes**: Botão cinza discreto no canto da tela
- **Depois**: Botão verde com ícone de "+" e texto claro, posicionado ao lado do painel de fila
- **Impacto**: Identificação imediata da funcionalidade

### Melhoria 2 — Campo de Prescrição Estruturado (P2)
- **Antes**: Campo de texto livre para toda a prescrição
- **Depois**: Subcampos separados para medicamento, dosagem e frequência, com botão "+ Adicionar medicamento"
- **Impacto**: Eliminação de ambiguidade no preenchimento

### Melhoria 3 — Indicação Visual de Obrigatoriedade (P3)
- **Antes**: Sem indicação visual
- **Depois**: Asterisco vermelho (*) nos campos obrigatórios e mensagem de validação inline
- **Impacto**: Redução de erros de preenchimento

### Melhoria 4 — Fonte do Painel de Espera (P4)
- **Antes**: Fonte de 24px para o nome do paciente chamado
- **Depois**: Fonte de 36px com negrito e cor de destaque
- **Impacto**: Leitura confortável a até 5 metros de distância

### Melhoria 5 — Máscara de CPF (P5)
- **Antes**: Campo sem formatação
- **Depois**: Máscara automática (XXX.XXX.XXX-XX) e validação de dígitos verificadores
- **Impacto**: Preenchimento mais rápido e com menos erros

## 5. Conclusão

Os testes de usabilidade revelaram que o protótipo do SaúdePOP é, em geral, intuitivo e de fácil aprendizado. As principais melhorias concentraram-se na visibilidade de ações frequentes e na estruturação de formulários complexos. Após as correções, espera-se que a taxa de sucesso na tarefa de registro de atendimento suba de 67% para próximo de 100%.
