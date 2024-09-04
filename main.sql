CREATE TABLE USER (
    user_id INT PRIMARY KEY,
    first_name NVARCHAR(50),
    last_name NVARCHAR(50),
    aadhar_no NVARCHAR(20),
    mobile_no NVARCHAR(15),
    email NVARCHAR(100),
    password NVARCHAR(50), -- In a real application, this would be hashed
    address NVARCHAR(255),
    city NVARCHAR(50),
    state NVARCHAR(50),
    pincode NVARCHAR(10),
    age INT,
    gender CHAR(1),
    security_ques NVARCHAR(255),
    security_ans NVARCHAR(255)
);
CREATE TABLE TRAIN (
    train_no INT PRIMARY KEY,
    train_name NVARCHAR(100),
    source NVARCHAR(100),
    destination NVARCHAR(100),
    departure_time TIME,
    arrival_time TIME
);
CREATE TABLE STATION (
    station_id INT PRIMARY KEY,
    name NVARCHAR(100),
    arrival_time TIME,
    halt_duration TIME,
    source NVARCHAR(100),
    destination NVARCHAR(100)
);
CREATE TABLE TRAIN_STATUS (
    train_no INT,
    date DATE,
    availability_of_seats INT,
    a_seats1 INT,
    b_seats1 INT,
    w_seats1 INT,
    a_seats2 INT,
    b_seats2 INT,
    w_seats2 INT,
    fare1 DECIMAL(10,2),
    fare2 DECIMAL(10,2),
    PRIMARY KEY (train_no, date),
    FOREIGN KEY (train_no) REFERENCES TRAIN(train_no)
);
CREATE TABLE TICKET (
    ticket_id INT PRIMARY KEY,
    train_no INT,
    booked_user INT,
    status NVARCHAR(50),
    no_of_passengers INT,
    FOREIGN KEY (train_no) REFERENCES TRAIN(train_no),
    FOREIGN KEY (booked_user) REFERENCES USER(user_id)
);
CREATE TABLE PASSENGER (
    passenger_id INT PRIMARY KEY,
    name NVARCHAR(100),
    gender CHAR(1),
    age INT,
    seat_number NVARCHAR(10),
    pnr_no NVARCHAR(20),
    ticket_id INT,
    FOREIGN KEY (ticket_id) REFERENCES TICKET(ticket_id)
);
CREATE TABLE TRAIN_STOPS_AT (
    train_no INT,
    station_id INT,
    PRIMARY KEY (train_no, station_id),
    FOREIGN KEY (train_no) REFERENCES TRAIN(train_no),
    FOREIGN KEY (station_id) REFERENCES STATION(station_id)
);
