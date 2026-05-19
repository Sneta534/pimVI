-- =============================================================================
-- SaúdePOP — Scripts DML (Inserções e Consultas)
-- =============================================================================

USE SaudePOP;
GO

-- =============================================================================
-- INSERÇÕES DE EXEMPLO
-- =============================================================================

-- Consultórios
INSERT INTO Consultorio (numero, andar, especialidade) VALUES (1, 1, 'Clínica Geral');
INSERT INTO Consultorio (numero, andar, especialidade) VALUES (2, 1, 'Clínica Geral');
INSERT INTO Consultorio (numero, andar, especialidade) VALUES (3, 1, 'Pediatria');
INSERT INTO Consultorio (numero, andar, especialidade) VALUES (4, 2, 'Ginecologia');

-- Profissionais de saúde
INSERT INTO Profissional (nome, crm, especialidade, telefone, email)
VALUES ('Dr. Carlos Mendes', 'CRM-SP 123456', 'Clínica Geral', '11999990001', 'carlos@clinica.com');

INSERT INTO Profissional (nome, crm, especialidade, telefone, email)
VALUES ('Dra. Paula Ferreira', 'CRM-SP 654321', 'Pediatria', '11999990002', 'paula@clinica.com');

INSERT INTO Profissional (nome, crm, especialidade, telefone, email)
VALUES ('Dra. Ana Souza', 'CRM-SP 111222', 'Ginecologia', '11999990003', 'ana@clinica.com');

INSERT INTO Profissional (nome, crm, especialidade, telefone, email)
VALUES ('Dr. Roberto Lima', 'CRM-SP 333444', 'Ortopedia', '11999990004', 'roberto@clinica.com');

-- Pacientes
INSERT INTO Paciente (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES ('Maria dos Santos', '12345678901', '1967-05-15', '11988880001', 'maria@email.com', 'Rua das Flores, 100 - São Paulo');

INSERT INTO Paciente (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES ('João Pedro Silva', '23456789012', '1990-08-22', '11988880002', 'joao@email.com', 'Av. Brasil, 500 - São Paulo');

INSERT INTO Paciente (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES ('Ana Luíza Costa', '34567890123', '1985-11-03', '11988880003', 'analu@email.com', 'Rua Esperança, 250 - São Paulo');

INSERT INTO Paciente (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES ('Pedro Rodrigues', '45678901234', '1972-02-28', '11988880004', 'pedro@email.com', 'Rua da Paz, 75 - São Paulo');

INSERT INTO Paciente (nome, cpf, data_nascimento, telefone, email, endereco)
VALUES ('Francisca Oliveira', '56789012345', '1955-09-10', '11988880005', NULL, 'Rua São Jorge, 310 - São Paulo');

-- Usuários do sistema
INSERT INTO Usuario (login, senha_hash, perfil, id_profissional)
VALUES ('juliana.recep', 'hash_senha_segura_1', 'recepcionista', NULL);

INSERT INTO Usuario (login, senha_hash, perfil, id_profissional)
VALUES ('dr.carlos', 'hash_senha_segura_2', 'medico', 1);

INSERT INTO Usuario (login, senha_hash, perfil, id_profissional)
VALUES ('admin', 'hash_senha_segura_3', 'admin', NULL);

-- Agendamentos
INSERT INTO Agendamento (id_paciente, id_profissional, id_consultorio, data_hora, status)
VALUES (1, 1, 1, '2025-03-15 08:00', 'realizado');

INSERT INTO Agendamento (id_paciente, id_profissional, id_consultorio, data_hora, status)
VALUES (2, 1, 1, '2025-03-15 08:15', 'realizado');

INSERT INTO Agendamento (id_paciente, id_profissional, id_consultorio, data_hora, status)
VALUES (3, 2, 3, '2025-03-15 08:30', 'agendado');

INSERT INTO Agendamento (id_paciente, id_profissional, id_consultorio, data_hora, status)
VALUES (4, 1, 1, '2025-03-15 08:45', 'falta');

-- Atendimentos
INSERT INTO Atendimento (id_paciente, id_profissional, id_agendamento, data_hora_inicio, data_hora_fim, anamnese, prescricao)
VALUES (1, 1, 1, '2025-03-15 08:05', '2025-03-15 08:20',
    'Paciente relata dores de cabeça frequentes há 2 semanas. PA elevada: 150/95 mmHg.',
    'Losartana 50mg - 1 comprimido ao dia. Retorno em 30 dias.');

INSERT INTO Atendimento (id_paciente, id_profissional, id_agendamento, data_hora_inicio, data_hora_fim, anamnese, prescricao)
VALUES (2, 1, 2, '2025-03-15 08:22', '2025-03-15 08:35',
    'Paciente com quadro gripal há 3 dias. Sem febre no momento.',
    'Dipirona 500mg - 1 comp. de 6/6h se dor. Repouso por 3 dias.');

-- Triagem
INSERT INTO Triagem (id_atendimento, pressao_arterial, temperatura, peso, altura)
VALUES (1, '150/95', 36.5, 72.00, 1.60);

INSERT INTO Triagem (id_atendimento, pressao_arterial, temperatura, peso, altura)
VALUES (2, '120/80', 37.2, 85.50, 1.78);

-- Fila
INSERT INTO Fila (id_paciente, id_consultorio, posicao, status, hora_entrada, prioridade)
VALUES (3, 3, 1, 'aguardando', '2025-03-15 08:25', 0);

INSERT INTO Fila (id_paciente, id_consultorio, posicao, status, hora_entrada, prioridade)
VALUES (5, 1, 1, 'aguardando', '2025-03-15 08:30', 1);

-- =============================================================================
-- CONSULTAS REPRESENTATIVAS
-- =============================================================================

-- 1. Buscar paciente por CPF
SELECT id_paciente, nome, cpf, data_nascimento, telefone
FROM Paciente
WHERE cpf = '12345678901';

-- 2. Listar agenda do dia de um profissional
SELECT a.data_hora, p.nome AS paciente, c.numero AS consultorio, a.status
FROM Agendamento a
INNER JOIN Paciente p ON a.id_paciente = p.id_paciente
INNER JOIN Consultorio c ON a.id_consultorio = c.id_consultorio
WHERE a.id_profissional = 1
  AND CAST(a.data_hora AS DATE) = '2025-03-15'
ORDER BY a.data_hora;

-- 3. Listar fila atual do consultório 1 (ordenada por prioridade e posição)
SELECT f.posicao, p.nome, f.status, f.hora_entrada, f.prioridade,
       DATEDIFF(MINUTE, f.hora_entrada, GETDATE()) AS minutos_espera
FROM Fila f
INNER JOIN Paciente p ON f.id_paciente = p.id_paciente
WHERE f.id_consultorio = 1
  AND f.status IN ('aguardando', 'chamado')
ORDER BY f.prioridade DESC, f.posicao ASC;

-- 4. Histórico de atendimentos de um paciente
SELECT a.data_hora_inicio, a.data_hora_fim, pr.nome AS profissional,
       pr.especialidade, a.anamnese, a.prescricao
FROM Atendimento a
INNER JOIN Profissional pr ON a.id_profissional = pr.id_profissional
WHERE a.id_paciente = 1
ORDER BY a.data_hora_inicio DESC;

-- 5. Estatísticas de atendimento por profissional (último mês)
SELECT pr.nome, pr.especialidade,
       COUNT(*) AS total_atendimentos,
       AVG(DATEDIFF(MINUTE, a.data_hora_inicio, a.data_hora_fim)) AS tempo_medio_min
FROM Atendimento a
INNER JOIN Profissional pr ON a.id_profissional = pr.id_profissional
WHERE a.data_hora_inicio >= DATEADD(MONTH, -1, GETDATE())
GROUP BY pr.nome, pr.especialidade
ORDER BY total_atendimentos DESC;

-- 6. Taxa de faltas por dia da semana
SELECT DATENAME(WEEKDAY, data_hora) AS dia_semana,
       COUNT(*) AS total_agendamentos,
       SUM(CASE WHEN status = 'falta' THEN 1 ELSE 0 END) AS total_faltas,
       CAST(SUM(CASE WHEN status = 'falta' THEN 1.0 ELSE 0 END) / COUNT(*) * 100 AS DECIMAL(5,2)) AS taxa_falta_pct
FROM Agendamento
GROUP BY DATENAME(WEEKDAY, data_hora), DATEPART(WEEKDAY, data_hora)
ORDER BY DATEPART(WEEKDAY, data_hora);

-- 7. Pacientes com mais faltas
SELECT p.nome, p.cpf, COUNT(*) AS total_faltas
FROM Agendamento a
INNER JOIN Paciente p ON a.id_paciente = p.id_paciente
WHERE a.status = 'falta'
GROUP BY p.nome, p.cpf
HAVING COUNT(*) >= 2
ORDER BY total_faltas DESC;

-- 8. Tempo médio de espera na fila por consultório
SELECT c.numero AS consultorio, c.especialidade,
       AVG(DATEDIFF(MINUTE, f.hora_entrada, f.hora_chamada)) AS tempo_medio_espera_min
FROM Fila f
INNER JOIN Consultorio c ON f.id_consultorio = c.id_consultorio
WHERE f.hora_chamada IS NOT NULL
GROUP BY c.numero, c.especialidade
ORDER BY c.numero;
