SELECT * FROM Students ORDER BY LastName ASC;
ALTER TABLE Students ADD gender VARCHAR(10);
UPDATE Students SET gender = 'Male'WHERE FirstName = 'Amit';
UPDATE Students SET gender = 'Female' WHERE FirstName = 'Priya';
UPDATE Students SET gender = 'Male' WHERE FirstName = 'Rahul';
UPDATE Students SET gender = 'Female' WHERE FirstName = 'Sneha';
SELECT * FROM Students;
SELECT gender, COUNT(*) AS count FROM Students GROUP BY gender;