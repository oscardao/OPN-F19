CREATE DATABASE takehome;

USE takehome

CREATE TABLE Person (
	PersonID int AUTO_INCREMENT PRIMARY KEY,
	Firstname text,
	Lastname text
);

INSERT INTO Person (Firstname, Lastname) VALUES ('Oscar', 'Dao');
