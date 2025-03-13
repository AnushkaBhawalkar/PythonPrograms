-- Step 1: Create the Database
create database StudentManagementSystem;
use StudentManagementSystem;
-- Step 2: Create Student Table
create table Student (StudentID int primary key auto_increment,FirstName varchar(50),LastName varchar(50));
-- Step 3: Insert 5 Records
insert into Student (FirstName, LastName)values('Amit', 'Sharma'),('Priya', 'Patel'),('Rahul', 'Verma'),('Sneha', 'Rao'),('Vikram', 'Singh');
-- Step 4: Alter Student Table to Add More Fields
alter table Student add column DateOfBirth date,
	add column Gender enum('Male', 'Female', 'Other'),
	add column Email varchar(100),
	add column Phone varchar(15);
-- Step 5: Update Newly Added Columns
update Student 
set DateOfBirth = '2000-01-15', Gender = 'Male', Email = 'amit.sharma@email.com', Phone = '9876543210'
where StudentID = 1;
update Student 
set DateOfBirth = '1998-12-05', Gender = 'Female', Email = 'sneha.rao@email.com', Phone = '9876543211'
where StudentID = 2;
update Student 
set DateOfBirth = '2001-03-10', Gender = 'Male', Email ='rahul.verma@email.com', Phone = '9876543212'
where StudentID = 3;
update Student 
set DateOfBirth = '1999-06-22', Gender = 'Female', Email = 'priya.patel@email.com', Phone = '9876543213'
where StudentID = 4;
update Student 
set DateOfBirth = '2000-08-30', Gender = 'Male', Email = 'vikram.singh@email.com', Phone = '9876543214'
where StudentID = 5;
-- Step 6: Create Course Table
create table Course (
    CourseID int primary key auto_increment,
    CourseTitle varchar(100),
    Credits int
);
-- Step 7: Create Instructor Table
create table Instructor (
    InstructorID int primary key auto_increment,
    FirstName varchar(50),
    LastName varchar(50),
    Email varchar(100)
);
-- Step 8: Create Enrollment Table
create table Enrollment (
    EnrollmentID int primary key auto_increment,
    EnrollmentDate date,
    StudentID int,
    CourseID int,
    InstructorID int,
    foreign key (StudentID) references Student(StudentID) on delete cascade,
    foreign key (CourseID) references Course(CourseID) on delete cascade,
    foreign key (InstructorID) references Instructor(InstructorID) on delete cascade
);
-- Step 9: Create Score Table
create table Score (
    ScoreID int primary key auto_increment,
    CourseID int,
    StudentID int,
    DateOfExam date,
    CreditObtained int,
    foreign key (CourseID) references Course(CourseID) on delete cascade,
    foreign key(StudentID) references Student(StudentID) on delete cascade
);

-- Step 10: Create Feedback Table
create table Feedback (
    FeedbackID int primary key auto_increment,
    StudentID int,
    Date date,
    InstructorName varchar(100),
    foreign key (StudentID) reference Student(StudentID) on delete cascade
);
