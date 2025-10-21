CREATE TABLE alunos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    matricula INT UNIQUE, 
    curso VARCHAR(50)
    );
#insere um aluno
INSERT INTO alunos (nome, matricula, curso)
VALUES ('bianca', 4444, 'ciencia de dados');
#seleciona um aluno
SELECT * FROM alunos;