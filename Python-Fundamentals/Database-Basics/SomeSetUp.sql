
--Using mariadb on Alma Linux 9*
--dnf update -y
--dnf install -y mariadb-server
--systemctl enable --now mariadb
--mysql_secure_installation
--mysql -u root -p

--Setting up User
create database softuni;

show databases;

GRANT ALL PRIVILEGES ON softuni.* TO 'softuni'@'localhost';

FLUSH PRIVILEGES;

DELETE FROM mysql.db WHERE User='softuni' AND Host='localhost' AND Db='homeworkSoftUni';

--View
select user, host from mysql.user;
--Table
SELECT * FROM mysql.global_priv WHERE User='softuni' AND Host='localhost';
--If Needed for user modification
UPDATE mysql.global_priv 
SET Host='localhost' 
WHERE User='softuni' AND Host='10.3.45.71';
FLUSH PRIVILEGES;

select user();

--Basic Queries
CREATE TABLE students (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
first_name VARCHAR(50) NULL, 
last_name VARCHAR(50) NULL, 
age INT NULL, 
grade DOUBLE NULL );

INSERT INTO students (first_name, last_name, age, grade) 
VALUES
('Guy', 'Gilbert', 15, 4.5),
('Kevin', 'Brown', 17, 5.4),
('Roberto', 'Tamburello', 19, 6),
('Linda', 'Smith', 18, 5),
('John', 'Stones', 16, 4.25),
('Nicole', 'Nelson', 17, 5.50);

ALTER TABLE students ADD email VARCHAR(50) NULL;
ALTER TABLE students MODIFY last_name VARCHAR(50) NOT NULL;

--Create 2nd table with relationship to students
CREATE TABLE towns (
townid INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
townname VARCHAR(30) NOT NULL );

describe towns;
--Create the foreign key to towns on students
ALTER TABLE students ADD COLUMN townid INT;
ALTER TABLE students ADD CONSTRAINT fk_townid FOREIGN KEY (townid) REFERENCES towns(townid);
describe students;
--To Check the current Constraints
show create table students;

INSERT INTO towns (townname)
VALUES
('Sofia'),
('Plovdiv'),
('Varna'),
('Burgas');

UPDATE students SET townid = 4 WHERE first_name = 'Linda' and last_name = 'Smith';
UPDATE students SET townid = 1 WHERE first_name = 'Kevin' and last_name = 'Brown';

--Perform an INNER JOIN => Returns if matches in ON condition
select s.first_name, s.last_name, s.age, t.townname
FROM students as s
JOIN towns as t ON s.townid = t.townid;

--Perform a LEFT JOIN => Includes all rows on the left table even there is no matches on the right table
select s.first_name, s.last_name, s.age, t.townname 
FROM students as s 
LEFT JOIN towns as t ON s.townid = t.townid;

--Perform a RIGHT JOIN => Includes all rows on the right table even there is no matches on the left table
select s.first_name, s.last_name, s.age, t.townname 
FROM students as s 
RIGHT JOIN towns as t ON s.townid = t.townid;

--Perform a CROSS JOIN => Includes all rows from the left table with all rows from the right table, typically used without ON condition
select s.first_name, s.last_name, s.age, t.townname 
FROM students as s 
CROSS JOIN towns as t;

--Now Let's implement 3rd table Countries, which should be a foreign key for towns
 CREATE TABLE countries (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
countryname VARCHAR(30) NOT NULL );

INSERT INTO countries (countryname) VALUES
('Bulgaria'),
('USA'),
('France'),
('Germany');
describe countries;
select * from countries;
--Foreign key
ALTER TABLE towns ADD COLUMN countryid INT;
ALTER TABLE towns ADD CONSTRAINT fk_country FOREIGN KEY (countryid) REFERENCES countries(id);
describe towns;
UPDATE towns SET countryid = 1 WHERE townname IN ('Sofia', 'Burgas');
UPDATE towns SET countryid = 4 WHERE townname = 'Plovdiv';

select s.first_name,
s.last_name,
s.age,
t.townname,
c.countryname
FROM
students AS s
JOIN
towns AS t ON s.townid = t.townid
JOIN
countries AS c ON t.countryid = c.id;


describe students;

select * from students;

select last_name, age, grade from students;

select * from students limit 5;

select last_name, grade from students limit 5;

truncate students;

drop table students;
