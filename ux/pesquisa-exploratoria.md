# Pesquisa Exploratória — SaúdePOP

## 1. Objetivo

Compreender a rotina, as necessidades e as dificuldades dos diferentes atores de uma clínica popular, a fim de embasar a concepção da experiência de uso do sistema SaúdePOP.

## 2. Metodologia

A pesquisa exploratória foi conduzida com base em três técnicas complementares:

1. **Entrevistas fictícias semiestruturadas** com representantes de cada perfil de usuário (paciente, recepcionista e profissional de saúde);
2. **Relatos de caso** baseados em cenários típicos observados em clínicas populares;
3. **Observação de cenário** descrevendo um dia típico de funcionamento da clínica.

---

## 3. Entrevistas Fictícias

### Entrevista 1 — Maria dos Santos, 58 anos (Paciente)

> **Entrevistador**: Dona Maria, como é a sua experiência quando vem à clínica?

> **Maria**: "Olha, eu venho todo mês por causa da pressão alta. Minha neta me traz de ônibus, a gente sai cedo pra garantir. O pior é que a gente chega às 7h e às vezes só é atendida às 10h. Não tem como saber quanto tempo vai demorar."

> **Entrevistador**: O que mais incomoda na espera?

> **Maria**: "Não saber. Se alguém me dissesse 'falta uma hora', eu ficava mais tranquila. Mas a gente fica ali sentada sem informação nenhuma. Outro dia uma senhora passou mal de tanto esperar em pé."

> **Entrevistador**: E quando entra no consultório?

> **Maria**: "O doutor me pergunta tudo de novo. Que remédio eu tomo, desde quando, se já fiz exame. Eu já falei tudo isso na consulta passada! Seria bom se ele já tivesse tudo anotado."

> **Entrevistador**: A senhora usa celular?

> **Maria**: "Uso sim, mas só WhatsApp e pra ligar. Minha neta que mexe nessas coisas de aplicativo. Se tivesse um telão na parede mostrando quem é o próximo, aí sim eu entenderia."

**Síntese**: Pacientes com baixa habilidade digital precisam de informações visuais claras e acessíveis (painel em tela grande). A falta de previsibilidade na espera gera ansiedade. Dados repetidos a cada consulta indicam ausência de prontuário eletrônico integrado.

---

### Entrevista 2 — Juliana Oliveira, 32 anos (Recepcionista)

> **Entrevistador**: Juliana, como é o seu dia a dia na recepção?

> **Juliana**: "É correria total. Eu atendo telefone, recebo paciente, cadastro, marco consulta, organizo a fila... tudo ao mesmo tempo. Em dia de pico eu atendo mais de 60 pessoas."

> **Entrevistador**: Qual a maior dificuldade?

> **Juliana**: "Quando dois pacientes aparecem com consulta no mesmo horário. No caderno de papel é difícil de ver conflito. E o prontuário... às vezes o papel sumiu, ou a letra do médico anterior é ilegível."

> **Entrevistador**: Como funciona a organização da fila?

> **Juliana**: "Eu anoto num papelzinho e vou gritando o nome. Mas paciente reclama que outro passou na frente, que eu favoreci alguém. Se tivesse um sistema que organizasse a fila automaticamente, com prioridade pra idoso e gestante, seria perfeito."

> **Entrevistador**: O que facilitaria seu trabalho?

> **Juliana**: "Poder cadastrar o paciente rápido, com poucos campos. Buscar por CPF em vez de ficar procurando pasta. E um botão de 'chamar próximo' que já mostra no telão da sala de espera."

**Síntese**: A recepcionista precisa de um sistema ágil, com cadastro simplificado, busca rápida por CPF, detecção de conflitos de horário e gestão automatizada de fila com prioridades.

---

### Entrevista 3 — Dr. Carlos Mendes, 45 anos (Médico Clínico Geral)

> **Entrevistador**: Doutor Carlos, como o senhor avalia o sistema atual?

> **Dr. Carlos**: "O sistema atual é papel. Prontuário em pasta de arquivo, prescrição em receituário de papel. Quando o paciente é novo, tudo bem. Mas paciente de retorno, eu preciso do histórico. E muitas vezes a pasta não está lá, ou a enfermeira anterior escreveu de forma ilegível."

> **Entrevistador**: Quanto tempo o senhor gasta buscando informações?

> **Dr. Carlos**: "Eu diria uns 3 a 5 minutos por paciente. Com 30 pacientes por dia, são quase 2 horas perdidas. Se eu tivesse um prontuário eletrônico com o histórico completo na tela, poderia ir direto ao que importa."

> **Entrevistador**: Como funciona a chamada dos pacientes?

> **Dr. Carlos**: "Eu dependo da Juliana. Ela grita o nome ou bate na porta. Às vezes eu fico esperando e ela está ocupada com outra coisa. Se eu pudesse clicar num botão e o paciente já fosse chamado no painel, seria muito mais eficiente."

> **Entrevistador**: O que o senhor espera de um sistema digital?

> **Dr. Carlos**: "Simplicidade. Quero abrir a tela, ver quem é o paciente, o histórico, registrar o atendimento em campos organizados e chamar o próximo. Em menos de 30 segundos entre um paciente e outro."

**Síntese**: O médico precisa de acesso rápido ao histórico, independência da recepção para chamar pacientes e um formulário de registro de atendimento que seja estruturado e rápido.

---

## 4. Relatos de Caso

### Caso 1 — "A consulta perdida"

Dona Francisca, 67 anos, agendou consulta para terça-feira às 9h. Por problemas de mobilidade, pediu ao filho que a levasse. O filho teve um imprevisto e ela chegou às 10h15. Na recepção, informaram que a consulta das 9h já tinha sido dada a outro paciente como "encaixe", pois o sistema de papel não tinha como notificá-la do atraso. Francisca voltou para casa sem atendimento.

**Oportunidade identificada**: Sistema de confirmação por WhatsApp 24h antes; registro de atraso com possibilidade de reencaixe na fila.

### Caso 2 — "O prontuário perdido"

João Pedro, 42 anos, é paciente de retorno com histórico de diabetes tipo 2. Na consulta, o médico não encontrou a pasta com o prontuário anterior. O paciente não se lembrava dos nomes dos medicamentos que tomava. O médico precisou fazer todo o levantamento novamente, consumindo 20 minutos da consulta de 15 minutos agendada.

**Oportunidade identificada**: Prontuário eletrônico com histórico completo e busca por CPF.

### Caso 3 — "A fila injusta"

Três pacientes aguardavam na sala de espera: uma gestante de 8 meses, um idoso de 75 anos e um jovem de 25 anos. O jovem havia chegado primeiro e foi atendido antes. A gestante e o idoso, que por lei deveriam ter prioridade, ficaram aguardando por mais 40 minutos. Não havia sistema de prioridade formalizado.

**Oportunidade identificada**: Sistema de fila com prioridade automática para idosos, gestantes, lactantes e PCDs, conforme legislação vigente.

---

## 5. Observação de Cenário — Um Dia Típico na Clínica

### 7h00 — Abertura

Juliana chega e abre a clínica. Confere o caderno de agendamentos e prepara as pastas dos prontuários dos pacientes do dia. Já há 4 pacientes esperando do lado de fora antes de abrir.

### 7h30 — Início dos atendimentos

Dr. Carlos chega e começa a atender. Juliana recebe os pacientes no balcão, confirma dados e adiciona à fila. A sala de espera tem 12 cadeiras e já está metade ocupada.

### 9h00 — Pico de movimento

Fila com 15 pessoas. Juliana atende telefone, recebe pacientes presenciais e tenta organizar encaixes. Um paciente reclama que está esperando há 1h30 sem informação. Juliana não tem como dizer quanto falta.

### 11h00 — Acúmulo

Dr. Carlos está com 15 minutos de atraso. Duas consultas se sobrepõem por conflito no caderno. Um paciente de retorno chega sem prontuário — a pasta foi arquivada errada.

### 12h00 — Fim do turno

Juliana contabiliza manualmente: 22 atendidos, 3 faltas, 2 encaixes. Anota no caderno de controle. Dr. Carlos reclama que 5 pacientes vieram sem histórico clínico acessível.

---

## 6. Síntese das Descobertas

| Descoberta | Impacto | Solução Proposta |
|---|---|---|
| Pacientes não têm informação sobre tempo de espera | Ansiedade, insatisfação, desistência | Painel de fila em tempo real com tempo estimado |
| Prontuários em papel são perdidos ou ilegíveis | Perda de tempo médico, risco clínico | Prontuário eletrônico com busca por CPF |
| Fila sem sistema de prioridade | Descumprimento legal, injustiça | Fila inteligente com prioridade automática |
| Recepcionista sobrecarregada | Erros de agendamento, conflitos | Sistema de gestão integrado com alertas |
| Médico depende da recepção para chamar pacientes | Perda de autonomia, atrasos | Botão "chamar próximo" no painel do médico |
| Dados repetidos a cada consulta | Tempo perdido, frustração do paciente | Cadastro único com histórico persistente |

Estas descobertas fundamentaram a criação das 3 personas e dos mapas de jornada, servindo como base para o design centrado no usuário do sistema SaúdePOP.
