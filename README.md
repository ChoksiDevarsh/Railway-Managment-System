# Railway-Managment-System
The Railway Management System is a desktop application developed using Python and Tkinter for the frontend, with SQL Server as the backend database. This application allows users to perform CRUD (Create, Read, Update, Delete) operations on railway records after a successful login.

Features
User Authentication: Ensures only authorized users can access the application. The default credentials are:
Username: admin
Password: password
CRUD Operations: Allows users to create, read, update, and delete records of trains, passengers, and stations.
Search Functionality: Users can search for specific records using various criteria.
Data Display: Uses a Treeview widget to display data in a tabular format, making it easy to view and manage records.
Responsive UI: Clean and intuitive interface designed with Tkinter, ensuring ease of use.
Installation
Prerequisites
Python 3.x
Tkinter (usually included with Python)
SQL Server
Steps
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/railway-management-system.git
cd railway-management-system
Install Required Packages:
Install the required Python packages using pip:

sh
Copy code
pip install pyodbc
Set Up SQL Server Database:

Open SQL Server Management Studio (SSMS).
Execute the provided SQL script to create the necessary database, tables, and stored procedures.
Run the Application:

sh
Copy code
python main.py
SQL Server Script
Ensure you run the following script in your SQL Server to set up the database, tables, and stored procedures:

sql
Copy code
-- Create the database if it does not already exist
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'PROJECT_DBMS_1')
BEGIN
    CREATE DATABASE PROJECT_DBMS_1;
END
GO

-- Use the database
USE PROJECT_DBMS_1;
GO

-- Create the train3 table if it does not already exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'train3')
BEGIN
    CREATE TABLE train3 (
        T_ID INT PRIMARY KEY,
        TrainName NVARCHAR(100),
        PassengerName NVARCHAR(100),
        PassengerID INT,
        Station NVARCHAR(100)
    );
END
GO

-- Insert sample data into the train3 table if it does not already exist
IF NOT EXISTS (SELECT * FROM train3 WHERE T_ID IN (1, 2))
BEGIN
    INSERT INTO train3 (T_ID, TrainName, PassengerName, PassengerID, Station) VALUES
    (1, 'Express Train', 'John Doe', 101, 'Station A'),
    (2, 'Local Train', 'Jane Smith', 102, 'Station B');
END
GO

-- Create the users table if it does not already exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'users')
BEGIN
    CREATE TABLE users (
        username NVARCHAR(50) PRIMARY KEY,
        password NVARCHAR(50)
    );
END
GO

-- Insert sample user data into the users table if it does not already exist
IF NOT EXISTS (SELECT * FROM users WHERE username = 'admin')
BEGIN
    INSERT INTO users (username, password) VALUES ('admin', 'password'); -- Note: In a real application, use hashed passwords
END
GO

-- Procedure to insert data
IF OBJECT_ID('InsertTrain', 'P') IS NULL
EXEC ('CREATE PROCEDURE InsertTrain
    @T_ID INT,
    @TrainName NVARCHAR(100),
    @PassengerName NVARCHAR(100),
    @PassengerID INT,
    @Station NVARCHAR(100)
AS
BEGIN
    INSERT INTO train3 (T_ID, TrainName, PassengerName, PassengerID, Station)
    VALUES (@T_ID, @TrainName, @PassengerName, @PassengerID, @Station);
END');
GO

-- Procedure to update data
IF OBJECT_ID('UpdateTrain', 'P') IS NULL
EXEC ('CREATE PROCEDURE UpdateTrain
    @T_ID INT,
    @TrainName NVARCHAR(100),
    @PassengerName NVARCHAR(100),
    @PassengerID INT,
    @Station NVARCHAR(100)
AS
BEGIN
    UPDATE train3
    SET TrainName = @TrainName, PassengerName = @PassengerName, PassengerID = @PassengerID, Station = @Station
    WHERE T_ID = @T_ID;
END');
GO

-- Procedure to delete data
IF OBJECT_ID('DeleteTrain', 'P') IS NULL
EXEC ('CREATE PROCEDURE DeleteTrain
    @T_ID INT
AS
BEGIN
    DELETE FROM train3
    WHERE T_ID = @T_ID;
END');
GO

-- Procedure to fetch all data
IF OBJECT_ID('FetchAllTrains', 'P') IS NULL
EXEC ('CREATE PROCEDURE FetchAllTrains
AS
BEGIN
    SELECT * FROM train3;
END');
GO

-- Procedure to fetch data by T_ID
IF OBJECT_ID('FetchTrainByID', 'P') IS NULL
EXEC ('CREATE PROCEDURE FetchTrainByID
    @T_ID INT
AS
BEGIN
    SELECT * FROM train3
    WHERE T_ID = @T_ID;
END');
GO

-- Procedure to check user credentials
IF OBJECT_ID('CheckUserCredentials', 'P') IS NULL
EXEC ('CREATE PROCEDURE CheckUserCredentials
    @username NVARCHAR(50),
    @password NVARCHAR(50)
AS
BEGIN
    SELECT COUNT(*) AS UserCount
    FROM users
    WHERE username = @username AND password = @password;
END');
GO
Usage
Login:
Enter the username and password (admin/password) to access the system.
CRUD Operations:
Add: Fill in the details and click 'Add' to insert a new record.
Update: Select a record, modify the details, and click 'Update' to save changes.
Delete: Select a record and click 'Delete' to remove it from the database.
Search: Enter search criteria and click 'Search' to find specific records.
