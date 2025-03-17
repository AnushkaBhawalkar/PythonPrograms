use studentmanagementsystem;
CREATE TABLE Instructor (InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    email VARCHAR(255) -- Including the email column directly
);
DESCRIBE Students;
select * from students;
SET SQL_SAFE_UPDATES = 0;

UPDATE Students SET email = 'amit_sharma@example.com' WHERE FirstName = 'Amit' AND LastName = 'Sharma';
UPDATE Students SET email = 'priya_verma@example.com' WHERE FirstName = 'Priya' AND LastName = 'Verma';
UPDATE Students SET email = 'rahul_kumar@example.com' WHERE FirstName = 'Rahul' AND LastName = 'Kumar';
UPDATE Students SET email = 'sneha_patel@example.com' WHERE FirstName = 'Sneha' AND LastName = 'Patel';
UPDATE Students SET email = 'vikas_singh@example.com' WHERE FirstName = 'Vikas' AND LastName = 'Singh';
DELETE FROM Students WHERE LastName = 'Singh';
SELECT * FROM Students WHERE FirstName LIKE 'R%';

CREATE TABLE Employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INT,
    email VARCHAR(255)
);
INSERT INTO Employee (first_name, last_name, age, email)
VALUES 
('John', 'Doe', 28, 'john.doe@example.com'),
('Jane', 'Smith', 35, 'jane.smith@example.com'),
('Roger', 'White', 40, 'roger.white@example.com');
UPDATE Employee SET age = age + 1 WHERE age > 25;
SELECT * FROM Employee;