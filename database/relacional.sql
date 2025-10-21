# Seleciona o banco de dados
USE db_relacional;
# Cria a tabela alunos
CREATE TABLE alunos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula INT UNIQUE,
    curso VARCHAR(50)
);
# Insere um aluno
INSERT INTO alunos (nome, matricula, curso)
VALUES ('Raysa Vale', '1234', 'Ciencias de dados');
# Selecionar um aluno
SELECT * FROM alunos;