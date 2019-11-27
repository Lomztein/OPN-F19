CREATE DATABASE 'opn';
USE 'opn';

CREATE TABLE 'persons' (
	'PersonID' INTEGER AUTO_INCREMENT,
	'Firstname' text,
	'Lastname' text,
	PRIMARY_KEY (PersonID)
);

INSERT INTO persons VALUES ("John", "Smith");
INSERT INTO persons VALUES ("Jane", "Doe");
