create database petshop
use petshop

create table petshop(
	id int primary key Identity,
	tipo_pet varchar(30),
	nome_pet varchar(30),
	idade int
);

select * from petshop
