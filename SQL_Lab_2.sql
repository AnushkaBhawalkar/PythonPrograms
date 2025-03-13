-- Modifying and Updating the Table Structure
create database school;
USE school;
create table student (rollno VARCHAR(10),name VARCHAR(5),class VARCHAR(5));
insert into student (rollno, name, class) values
('101', 'Amit', '10A'),
('102', 'Anil', '10B'),
('103', 'Rahul', '10A'),
('104', 'Rita', '10C'),
('105', 'Sita', '10B'),
('106', 'Arun', '10A'),
('107', 'Ravi', '10C'),
('108', 'Asha', '10B'),
('109', 'Kiran', '10A'),
('110', 'Meera', '10C');

-- Retrieve all students whose names start with the letter 'A'
SELECT * FROM student WHERE name LIKE 'A%';
-- Display all students who belong to class '10A'
SELECT * FROM student WHERE class = '10A';
-- Fetch the total number of students in each class
SELECT class, COUNT(*) AS total_students FROM student GROUP BY class;
-- Select students whose roll number contains '123' anywhere in it
SELECT * FROM student WHERE rollno LIKE '%123%';
-- Retrieve distinct class names
SELECT DISTINCT class FROM student;

-- Querying the Table
-- Retrieve all students whose names start with the letter 'A'
SELECT * FROM student WHERE name LIKE 'A%';
-- Display all students who belong to class '10A'
SELECT * FROM student WHERE class = '10A';
-- Fetch the total number of students in each class
SELECT class, COUNT(*) AS total_students FROM student GROUP BY class;
-- Select students whose roll number contains '123' anywhere in it
SELECT * FROM student WHERE rollno LIKE '%123%';
-- Retrieve distinct class names
SELECT DISTINCT class FROM student;

-- Create a Marks Table & Perform Queries
-- Create a 'marks' table
CREATE TABLE marks (
    rollno INT,
    marks INT,
    FOREIGN KEY (rollno) REFERENCES student(rollno) ON DELETE CASCADE
);
-- Insert sample marks
INSERT INTO marks (rollno, marks) VALUES
(101, 85),
(102, 78),
(103, 92),
(104, 67),
(105, 81),
(106, 89),
(107, 95),
(108, 72),
(109, 88),
(110, 90);
-- Retrieve the highest marks obtained by any student
SELECT MAX(marks) AS highest_marks FROM marks;
-- List students who scored more than 80 marks
SELECT student.* FROM student 
JOIN marks ON student.rollno = marks.rollno
WHERE marks > 80;
-- Find the average marks of students in each class
SELECT student.class, AVG(marks) AS average_marks 
FROM student 
JOIN marks ON student.rollno = marks.rollno
GROUP BY student.class;
-- Retrieve details of students who do not have marks recorded
SELECT * FROM student 
WHERE rollno NOT IN (SELECT rollno FROM marks);

--  Subqueries & Sorting
-- Find students who have the second-highest marks
SELECT * FROM student 
WHERE rollno = (SELECT rollno FROM marks ORDER BY marks DESC LIMIT 1 OFFSET 1);
-- Retrieve the top 5 students based on their marks
SELECT student.*, marks.marks FROM student 
JOIN marks ON student.rollno = marks.rollno
ORDER BY marks DESC 
LIMIT 5;
-- Display students sorted by name (ASC) and class (DESC)
SELECT * FROM student ORDER BY name ASC, class DESC;
