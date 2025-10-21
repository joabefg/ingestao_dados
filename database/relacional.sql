# seleciona banco de dados
USE db_relacional;
# cria a tabela alunos
CREATE TABLE alunos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    MATRICULA INT UNIQUE,
    curso VARCHAR(50)
);
# INSERE UM ALUNO
INSERT INTO alunos (nome, matricula, curso)
VALUES ('Joseph faustino', 1234, 'ciencia de dados');
# seleciona um aluno
SELECT * FROM alunos;