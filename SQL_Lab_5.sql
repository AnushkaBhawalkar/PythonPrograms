use studentmanagementsystem;
CREATE TABLE Enrollment (
    EnrollmentID INT PRIMARY KEY,
    StudentID INT,
    CourseName VARCHAR(100),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);
INSERT INTO Enrollment (EnrollmentID, StudentID, CourseName) VALUES 
(101, 1, 'Math'),
(102, 1, 'History'),
(103, 2, 'Physics'),
(104, 2, 'Chemistry');
SELECT s.StudentID, s.FirstName, s.LastName, e.EnrollmentID, e.CourseName FROM Students s
RIGHT JOIN Enrollment e ON s.StudentID = e.StudentID;

SELECT * FROM Students;
SELECT * FROM Enrollment;
DELETE FROM Enrollment WHERE EnrollmentID = 101;
INSERT IGNORE INTO Enrollment (EnrollmentID, StudentID, CourseName) VALUES 
(101, 1, 'Math'),
(102, 1, 'History'),
(103, 2, 'Physics'),
(104, 3, 'Chemistry'),
(105, 4, 'English');
SELECT s.StudentID, s.FirstName, s.LastName, s.email, e.EnrollmentID, e.CourseName FROM Students s
LEFT JOIN Enrollment e ON s.StudentID = e.StudentID;