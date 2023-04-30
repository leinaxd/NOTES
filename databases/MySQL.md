

source:
    FREECODECAMP:
    https://www.youtube.com/watch?v=HXV3zeQKqGY
# Install MySQL in linux

https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-es

Descarga e instalación
```
sudo apt update
sudo apt install mysql-server
```
Testear
```
sudo mysql
    -> create database [your database name]
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

sudo mysql -u root -p
    -> SHOW DATABASES;
    -> USE mysql #or any of your databases
    -> show tables;

sudo mysql -h 127.0.0.1 -u root -p #local host

```


Inicializacion del servidor
```
sudo mysql
sudo mysql_secure_instalation 
```


### Prueba 1 DATABASE SCHEMA

```
mysql> CREATE DATABASE testdb
mysql> CREATE TABLE student(
    student_id INT PRIMARY KEY,
    name VARCHAR(20),
    major VARCHAR(20)
    );

mysql> SHOW TABLES;
mysql> DESCRIBE student;
mysql> DROP student; #Elimina la tabla
```


### Prueba 2: Inserting DATA
```
mysql> CREATE TABLE student_2(
    student_id INT,
    name VARCHAR(20) NOT NULL, #This field cannot be null
    major VARCHAR(20) UNIQUE,
    PRIMARY KEY(student_id) #Note you can set primary key here
    );

mysql> ALTER TABLE student ADD gpa DECIMAL(3,2);
mysql> ALTER TABLE student DROP gpa;


INSERT INTO student VALUES(1, 'Jack', 'Biology');
INSERT INTO student VALUES(2, 'Kate', 'Sociology');
INSERT INTO student VALUES(3, NULL, 'Chemistry');  #invalid name
INSERT INTO student(student_id, name) VALUES(3, 'Claire'); #some fields are missing
INSERT INTO student VALUES(4, 'Jack', 'Biology');
INSERT INTO student VALUES(5, 'Mike', 'Computer Science');
#You cannot insert the same primary key value


SELECT * FROM student; #shows all the info about student
```
PRIMARY KEY == NOT NULL + UNIQUE

Constrains: 
    NOT NULL
    UNIQUE
    DEFAULT '<default value>'
    AUTO_INCREMENT

### Prueba 2: UPDATE & DELETE
```
UPDATE student
SET major ='Bio'
WHERE major = 'Biology';

UPDATE student
SET name = 'Tom', major='undecided'
WHERE student_id = 3;

UPDATE student
SET major = 'Biochemistry'
WHERE major = 'Bio' or major = 'Chemistry';

#update all rows
UPDATE student
SET major = 'undecided';

#Delete specific row
DELETE FROM student
WHERE student_id=5;
```

Where allows you to filter some data

### Prueba 3: Get information from the table
```
SELECT * 
FROM student
LIMIT 2;

SELECT name, major
FROM student;

SELECT student.name, student.major
FROM student
ORDER BY name ASC / DESC;

SELECT student.name, student.major
FROM student
ORDER BY major, name;

SELECT *
FROM student
WHERE name IN ('Claire','Mike')
``` 
Other operations:
    -- Comment
    OR AND <= >= < > <> =
    IN

# Prueba 4: Company SCHEMA
```
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birth_date DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT, #FOREIGN ID
    branch_id INT #FOREIGN ID
    );

CREATE TABLE branch(
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT, #Manager
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
    );

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY (super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;


CREATE TABLE client(
client_id INT PRIMARY KEY,
client_name VARCHAR(40),
branch_id INT,
FOREIGN KEY (branch_id) 
REFERENCES branch (branch_id)
ON DELETE SET NULL);


CREATE TABLE works_with(
    emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY (emp_id, client_id),
    FOREIGN KEY (emp_id) REFERENCES employee(emp_id) ON DELETE CASCADE, #Note set is not required
    FOREIGN KEY (client_id) REFERENCES client(client_id) ON DELETE CASCADE);

CREATE TABLE branch_supplier(
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY (branch_id, supplier_name),
    FOREIGN KEY (branch_id) REFERENCES branch (branch_id) ON DELETE CASCADE);


-- Load data
INSERT INTO employee VALUES (100, 'david', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL); 
--Branch should be 1, but branch isn't created yet.

INSERT INTO branch VALUES (1, 'Corporate', 100, '2006-02-09')

-- now you do update employee branch
UPDATE employee
SET branch_id = 1
WHERE emp_id = 100;

INSERT INTO employee VALUES (101, 'Jan', 'Levinson', '1961-05-11', 'F', 1100000, 100, 1);


INSERT INTO employee VALUES (102, 'Michael', 'Scott', '1964-03-15', 'M', 250000, NULL, NULL); 
INSERT INTO branch VALUES (2, 'Scranton', 102, '1992-04-06');
UPDATE employee
SET branch_id=2
WHERE emp_id=102;

INSERT INTO employee VALUES (103, 'Angela', 'Martin', '1971-06-25', 'F', 10000, NULL, 2);
INSERT INTO employee VALUES (104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, NULL, 2);
INSERT INTO employee VALUES (105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, NULL, 2);
INSERT INTO employee VALUES (106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, NULL, Null);
INSERT INTO employee VALUES (107, 'Andy', 'Bernard', '1973-07-22', 'M', 65000, NULL, Null);
INSERT INTO employee VALUES (108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, NULL, Null);

INSERT INTO branch VALUES (3, 'Stamford', 106, '1998-02-13');
UPDATE employee
SET branch_id=3
WHERE emp_id=106 OR emp_id =107 OR emp_id=108;


INSERT INTO branch_supplier VALUES (2, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES (2, 'Uni-ball', 'Writing utensils');
INSERT INTO branch_supplier VALUES (3, 'Patriot Paper', 'Paper');
INSERT INTO branch_supplier VALUES (2, 'J.T. Forms &we Labels', 'Custom Forms');
INSERT INTO branch_supplier VALUES (3, 'Uni-ball', 'Writing utensils');
INSERT INTO branch_supplier VALUES (3, 'Hammer Mill', 'Paper');
INSERT INTO branch_supplier VALUES (3, 'Stamford Labels', 'Custom Forms');

INSERT INTO client VALUES(400, 'Dunmore Highschool', 2);
INSERT INTO client VALUES(401, 'Lackawana Country', 2);
INSERT INTO client VALUES(402, 'FedEx', 3);
INSERT INTO client VALUES(403, 'John Daily Law LLC', 3);

INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
```

NOTES:
    I forgot to set primary key in branch.
    SO
    ```
    ALTER TABLE branch ADD PRIMARY KEY (branch_id); 
    ```

### Prueba 5: More basic queries
```
-- find all employees
SELECT * 
FROM employee
ORDER BY salary DESC;

SELECT * 
FROM employee
ORDER BY sex, first_name, last_name
LIMIT 5;

SELECT first_name, last_name
FROM employee;

SELECT first_name AS forename, last_name AS surname
FROM employee;

SELECT DISTINCT sex
FROM employee;
```
### Prueba 6: Functions
```
-- find the number of employees
SELECT COUNT(emp_id) 
FROM employee;

--find the number of female employees born after 1970
SELECT COUNT(emp_id)
FROM employee
WHERE sex ='F' AND birth_date > '1970-01-01';

-- find the average of all employee's salaries
SELECT AVG (salary)
FROM employee;

-- find the sum of all male employee's salaries
SELECT AVG (salary)
FROM employee
WHERE sex = 'M';

-- find hwo many males and females there are?
SELECT COUNT(sex), sex
FROM employee
GROUP BY sex;

-- find the total sales of each salesman
SELECT SUM(total_sales), emp_id
FROM works_with
GROUP BY emp_id;

-- same but for clients
SELECT SUM(total_sales), client_id
FROM works_with
GROUP BY client_id;

-- % any characters, _ one char
-- find any client's who are an LLC
SELECT *
FROM client
WHERE client_name LIKE '%LLC';

-- find any employee born in octuber
SELECT *
FROM employee
WHERE birth_date LIKE '____-10%'; #match any 4 chars, then 10 then any

-- find any clients who are schools
SELECT * 
FROM client
WHERE client_name LIKE '%school%';
```

### Prueba 7: Unions
```
-- find a list of employee and branch names
SELECT first_name 
FROM employee
UNION
SELECT branch_name
FROM branch
UNION
SELECT client_name
FROM client;

#RULES
1. Same num of cols in each select statement
2. Same datatype
3. The first one gets the name of the column

SELECT first_name , last_name #Error
FROM employee
UNION
SELECT branch_name
FROM branch;

-- find a list of all clients & 'branch suppliers' names
SELECT client_name, branch_id
FROM client
UNION 
SELECT supplier_name, branch_id
FROM branch_supplier;

-- Prefix with column names
SELECT client_name, client.branch_id
FROM client
UNION 
SELECT supplier_name, branch_supplier.branch_id
FROM branch_supplier;

-- find a list of all money earn of spent by the company
SELECT salary
FROM employee
UNION
SELECT total_sales
FROM works_with;
```

### Prueba 8: Joins
Combines rows from many tables
```
INSERT INTO branch VALUES (4, 'Buffalo', NULL, NULL);

-- find all branches and the names of their managers (INNER JOIN)
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
JOIN branch
ON employee.emp_id = branch.mgr_id; 
-- Joins tables merging ON <col>

-- LEFT JOIN (all employees are included, even when they don't have a branch_name)
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
LEFT JOIN branch
ON employee.emp_id = branch.mgr_id; 

-- RIGHT JOIN (Same but include all branches)
SELECT employee.emp_id, employee.first_name, branch.branch_name
FROM employee
RIGHT JOIN branch
ON employee.emp_id = branch.mgr_id; 

-- FULL OUTHER JOIN (not available in MySQL, is left+right join)
```


### Prueba 9: Nested Queries
```
-- find names of all employees who have
-- sold over 30000 to a single client
SELECT works_with.emp_id
FROM works_with
WHERE works_with.total_sales > 30000;


-- From those employees list take first_name and last_name
SELECT employee.first_name, employee.last_name
FROM employee
WHERE employee.emp_id IN (
    SELECT works_with.emp_id
    FROM works_with
    WHERE works_with.total_sales > 30000
    );

-- Find all clients who are handled by the branch
-- that Michael Scott manages
-- Assume you know Michael's ID
SELECT client.client_name
FROM client
WHERE client.branch_id = (
    SELECT branch_id 
    FROM branch
    WHERE branch.mgr_id = 102
    LIMIT 1
    );
```

### Prueba 10: ON DELETE
```
-- imagine we are going to delete michael scott emp_id=102.
--  the mgr_id is linking a row in the branch table

ON DELETE SET NULL
-- The mgr_id sets to null
ON DELETE CASCADE
-- Delete the entire row

CREATE TABLE branch(
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY (mgr_id) REFERENCES employee (mgr_id) ON DELETE SET NULL);

DELETE FROM employee 
WHERE emp_id = 102;
SELECT * FROM branch;

CREATE TABLE branch_supplier(
    branch_id INT,
    supplier_name VARCHAR(40),
    supply_type VARCHAR(40),
    PRIMARY KEY (branch_id, supplier_name),
    FOREIGN KEY (branch_id) REFERENCES branch (branch_id) ON DELETE CASCADE
    );

SELECT * FROM branch_supplier;
DELETE FROM branch
WHERE branch_id = 2;
SELECT * FROM branch_supplier;


-- NOTE. If you delete an item used as a PRIMARY KEY, you cannot acces the table anymore so cascade it.
--      and delete the entire row for that other table
```

### Prueba 11: TRIGGERS
```
-- Actions when data is mutated

CREATE TABLE trigger_test(
    message VARCHAR (100)
    );

-- Change the delimiter to $$ instead of ;
DELIMITER $$
    CREATE
    TRIGGER my_trigger BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO triger_test VALUES('added new employee');
    END $$
DELIMITER;

INSERT INTO employee VALUES(109, 'Oscar', 'Martinez', '1968-02-19', 'M', 69000,106,3);
SELECT * FROM trigger_test;


-- NEW row beign inserted
DELIMITER $$

CREATE
TRIGGER my_trigger_1 BEFORE INSERT
ON employee
FOR EACH ROW BEGIN
    INSERT INTO trigger_test VALUES(NEW.first_name);
END $$

DELIMITER ;

INSERT INTO employee VALUES(110, 'Kevin', 'Malone', '1978-02-19', 'M', 69000,106,3);
SELECT * FROM trigger_test;


-- IF THEN ELSE
DELIMITER $$
CREATE
    TRIGGER my_trigger_2 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        IF NEW.sex = 'M' THEN
            INSERT INTO trigger_test VALUES('added male employee');
        ELSEIF NEW.sex = 'F' THEN 
            INSERT INTO trigger_test VALUES('added female employee');
        ELSE
            INSERT INTO trigger_test VALUES('added other gender employee');
        END IF;
    END$$
DELIMITER ;
SELECT * FROM trigger_test;

INSERT INTO employee VALUES (111, 'Pam', 'Beesly', '1998-02-19', 'F', 69000, 106, 3);


-- You can also create triggers for
-- BEFORE/AFTER INSERT
-- BEFORE/AFTER DELETE
-- BEFORE/AFTER UPDATE

DROP TRIGGER my_trigger_2;
```

### Prueba 12: ER DIAGRAMS INTRO
Entity relations
Design a DATABASE SCHEMA
- Entity: object we want to model
        Square
- Attribute: Specific information about entity
    Ovals connected to your squared entity:
- Primary Key:  Normal attribute
    Colored ovals

- Composite Attributes: can be splitted
    (name: first_name + last_name)
- Multi valued attributes: attributes with more than 1 value
    (double circled attributed, a student may belong to multiple clubs)
- Derived Attributes: can be infered from other attributes
    (dashed lines oval, has honors? check grades)
- Multiple entities:
    class_id: 
    - Relationship between entities
    Student is related to the class
    The class is taken by a student
    (rhomb figure)
    - All classes must have a student relation (unless ghost classes)

    - Relationship attribute:
        An attribute about a relationship
        (Grade for a class, not stored in the student nor the class. The grade is stores into the relationship)
    - Relationship cardinality:
        number of instances of an entity from a 
        relation that can be assosiated with the
        relation.
        (1: 1, one to one, 1:N, N:M)
        A 1 student can take any number M of clases
        A class is taken by any number of student
    - Weak entities
        Entity cannot be identified by its own attributes
        A class can have an exam. But an exam doens't exist without a class.
```

```
