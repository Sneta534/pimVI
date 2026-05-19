# CONCLUSÃO

O presente trabalho apresentou o projeto do sistema **SaúdePOP**, um ecossistema web voltado para clínicas populares que integra prontuário eletrônico simplificado, agendamento de consultas, gestão de filas em tempo quase real e módulos de análise de dados preditiva.

O desenvolvimento do projeto permitiu a aplicação prática e integrada dos conhecimentos adquiridos nas quatro disciplinas do semestre:

Na disciplina de **Engenharia de Software Ágil Aplicada**, foram elaborados o documento de visão e escopo, os requisitos funcionais e não funcionais, o backlog de produto em formato de user stories, o planejamento de três sprints e o plano de verificação e validação com casos de teste documentados. A adoção do Scrum e do Kanban proporcionou organização e visibilidade ao andamento do projeto, e a definição de critérios de aceite garantiu foco na qualidade das entregas.

Na disciplina de **Modelagem de Banco de Dados e NoSQL**, foi projetado um modelo relacional normalizado até a terceira forma normal, com oito entidades interligadas que sustentam todas as operações do sistema. Os scripts DDL e DML para SQL Server foram implementados com índices otimizados para as consultas mais frequentes. O módulo NoSQL complementou o modelo relacional, armazenando logs de acesso, anotações livres e eventos de fila em formato de documentos JSON, atendendo à flexibilidade exigida por esses tipos de dados.

Na disciplina de **UX e UI Design**, a pesquisa com personas e mapas de jornada identificou as necessidades e frustrações dos três perfis de usuário — paciente, recepcionista e profissional de saúde. Os wireframes e o fluxo de navegação foram desenhados com foco em simplicidade e eficiência, e os testes de usabilidade com usuários simulados revelaram melhorias que foram incorporadas ao protótipo, como o destaque visual de botões de ação e a reformulação do campo de prescrição.

Na disciplina de **Machine Learning e Análise de Dados**, foi construído um pipeline completo de análise preditiva, desde a preparação do dataset simulado até o treinamento e avaliação de modelos de classificação (previsão de faltas) e regressão (estimativa de tempo de espera). O modelo Random Forest, após ajuste de hiperparâmetros, alcançou AUC-ROC de 0,86 na previsão de no-show, e o Gradient Boosting atingiu erro médio de 6,2 minutos na estimativa de tempo de espera, resultados que demonstram a viabilidade da aplicação de técnicas de aprendizado de máquina no contexto de clínicas populares.

Conclui-se que o sistema proposto tem potencial para reduzir significativamente os problemas operacionais enfrentados por clínicas populares, contribuindo para a melhoria do atendimento ao paciente, a eficiência da equipe administrativa e a qualidade das decisões gerenciais baseadas em dados. Como trabalhos futuros, recomenda-se a validação do sistema com dados reais e a expansão dos modelos preditivos com variáveis externas, além da implementação de um módulo de telemedicina.
