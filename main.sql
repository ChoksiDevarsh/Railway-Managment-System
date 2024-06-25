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
