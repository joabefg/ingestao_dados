USE db_relacional;

CREATE table alunos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    matricula INT UNIQUE,
    curso VARCHAR(50)
);

  INSERT INTO alunos (nome, matricula, curso)
  values ('jonathan', 1234, 'ciencia de dados');
  
  select * from alunos; 