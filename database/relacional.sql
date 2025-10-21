# seleciona o banco de dados
USE db_relacional;
# criar a tabela alunos
CREATE TABLE alunos (
	id INT auto_increment primary KEY,
    nome varchar(100) NOT NULL,
    matricula INT unique,
    curso varchar(50)
);
# insere um alunos
INSERT INTO alunos (nome, matricula, curso)
VALUES ('guilherme', 1234, 'ciencia de dados');
# seleciona um aluno
SELECT * FROM alunos;