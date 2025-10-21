use db_relacional;

CREATE TABLE alunos(
	id INT auto_increment primary key,
    nome varchar(100) not null,
    matricula int unique,
    curso varchar(50)
);
#insere um aluno
insert into alunos (nome, matricula, curso)
values ('Danilo', 1234, 'ciencia de dados');
#seleciona um aluno
select * from alunos;