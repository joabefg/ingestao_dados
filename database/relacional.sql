# seleciona o banco de dados
USE db_relacional;
# cria tabela de alunos
CREATE TABLE alunos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula INT UNIQUE, 
    curso VARCHAR(50)
);
# insere um aluno]
INSERT INTO alunos (nome,matricula,curso) 
VALUES  ('Paula', 0814, 'ciencia de dados');
# seleciona um aluno
SELECT * FROM alunos;