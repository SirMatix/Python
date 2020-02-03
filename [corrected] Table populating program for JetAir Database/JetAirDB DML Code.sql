DROP DATABASE IF EXISTS JetAirDB; 

CREATE DATABASE IF NOT EXISTS JetAirDB;

USE JetAirDB;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

CREATE TABLE Country
(
	CountryID INT(10) AUTO_INCREMENT PRIMARY KEY,
	Country VARCHAR(50)
);

CREATE TABLE City
(
	CityID INT(10) AUTO_INCREMENT PRIMARY KEY,
	City_name VARCHAR(50),
	CountryID INT(10),
	CONSTRAINT FOREIGN KEY CountryID(CountryID)
    REFERENCES Country(CountryID)
);

CREATE TABLE Postcode 
(
	PostcodeID INT(10) AUTO_INCREMENT PRIMARY KEY,
	Postcode VARCHAR(10),
	CityID INT(10),
	CONSTRAINT FOREIGN KEY CityID(CityID)
	REFERENCES City(CityID)
);


CREATE TABLE Passanger
(
    Pass_id INT(6) AUTO_INCREMENT PRIMARY KEY,
	Pass_first_name VARCHAR(25),
	Pass_last_name VARCHAR(25),
	Pass_dob DATE,
	Pass_phone_no VARCHAR(15),
	Pass_street_number VARCHAR(10),
	Pass_street_name VARCHAR(50),
	CityID INT(10),
	PostcodeID INT(10),
	CONSTRAINT FOREIGN KEY fkCityID(CityID)
	REFERENCES City(CityID),
	CONSTRAINT FOREIGN KEY fkPostcodeID(PostcodeID)
	REFERENCES Postcode(PostcodeID),
	PPassport_n VARCHAR(50)
);

CREATE TABLE Plane_model
(	
	PmodelID INTEGER(6) AUTO_INCREMENT PRIMARY KEY,
	Ptype VARCHAR(25),
	Pmodel VARCHAR(25),
	PNumOfPass INTEGER(3),
	Pproducent VARCHAR(50)
);

ALTER TABLE `plane_model` ADD INDEX(`Ptype`);

CREATE TABLE Plane
(
	PlaneID INT(6) AUTO_INCREMENT PRIMARY KEY,
	PmodelID INTEGER(6),
	CONSTRAINT FOREIGN KEY fk_PmodelID(PmodelID)
	REFERENCES Plane_model(PmodelID),
	Plane_purchasedate DATE,
	Plane_insurancedate DATE,
	Plane_price_paid INTEGER(9)
);


CREATE TABLE Airports
(
	AirportID VARCHAR(10) PRIMARY KEY,
	Airport_name VARCHAR(255),
	AStreetname VARCHAR(50),
	CityID INT(10),
	PostcodeID INT(10),
	CONSTRAINT FOREIGN KEY fk_CityID(CityID)
	REFERENCES City(CityID),
	CONSTRAINT FOREIGN KEY fk_PostcodeID(PostcodeID)
	REFERENCES Postcode(PostcodeID)
);

CREATE TABLE Route
(
	RouteID INT(3) AUTO_INCREMENT PRIMARY KEY,
	Airport_depart VARCHAR(10),
	Airport_arrival VARCHAR(10),
	CONSTRAINT FOREIGN KEY fk_Airport_depart(Airport_depart)
	REFERENCES Airports(AirportID),
	CONSTRAINT FOREIGN KEY fk_Airport_arrival(Airport_arrival)
	REFERENCES Airports(AirportID)
);

CREATE TABLE Flight
(
	Flight_id INT(10) AUTO_INCREMENT PRIMARY KEY,
	PlaneID INT(6),
	RouteID INT(6),
	CONSTRAINT FOREIGN KEY fk_PlaneID(PlaneID)
	REFERENCES Plane(PlaneID),
	CONSTRAINT FOREIGN KEY fk_RouteID(RouteID)
	REFERENCES Route(RouteID),
	Flight_date DATE,
	Flight_dep_time TIME,
	Flight_arr_time TIME,
	FNumOfPass INTEGER(3)
);

CREATE TABLE Price
(
	PriceID INT(10) AUTO_INCREMENT PRIMARY KEY,
	Price INTEGER(3),
	RouteID INT(6),
	CONSTRAINT FOREIGN KEY fk_RouteID2(RouteID)
	REFERENCES Route(RouteID),
	Seat_num_from INT(2),
	Seat_num_to INT(2)
);

CREATE TABLE Employee
(
	E_id INT(6) AUTO_INCREMENT PRIMARY KEY,
	E_first_name VARCHAR(25),
	E_last_name VARCHAR(25),
	E_dob DATE, 
	E_phone_no VARCHAR(15),
	E_street_number VARCHAR(10),
	E_street_name VARCHAR(50),
	CityID INT(10),
	PostcodeID INT(10),
	CONSTRAINT FOREIGN KEY fke_CityID(CityID)
	REFERENCES City(CityID),
	CONSTRAINT FOREIGN KEY fke_PostcodeID(PostcodeID)
	REFERENCES Postcode(PostcodeID),
	E_salary INTEGER(5),
	Position VARCHAR(20)
);



CREATE TABLE Ticket
(
	Ticket_id INT(10) AUTO_INCREMENT PRIMARY KEY,
	Pass_ID INT(6),
	CONSTRAINT FOREIGN KEY fk_Pass_id(Pass_id)
	REFERENCES Passanger(Pass_id),
	Flight_id INT(3),
	CONSTRAINT FOREIGN KEY fk_Flight_id(Flight_id)
	REFERENCES Flight(Flight_id),
	Seat_number VARCHAR(6),
	PriceID INT(3),
	CONSTRAINT FOREIGN KEY fk_PriceID(PriceID)
	REFERENCES Price(PriceID),
	Ticket_date DATE
);
    

CREATE TABLE Reservations
(
	Reservation_ID INT(10) AUTO_INCREMENT PRIMARY KEY,
	Pass_id INT(6),
	CONSTRAINT FOREIGN KEY fkr_Pass_ID(Pass_id)
	REFERENCES Passanger(Pass_id),
	Flight_id INT(6),
	CONSTRAINT FOREIGN KEY fkr_Flight_id(Flight_id)
	REFERENCES Flight(Flight_id),
	Ticket_id INT(10),
	CONSTRAINT FOREIGN KEY fkr_Ticket_id(Ticket_id)
	REFERENCES Ticket(Ticket_id),
	Res_Status VARCHAR(30)
);



CREATE TABLE Qualification
(
	Qualification_id INT(6) AUTO_INCREMENT PRIMARY KEY,
	Ptype VARCHAR(25),
	CONSTRAINT FOREIGN KEY fk_Ptype(Ptype)
	REFERENCES Plane_model(Ptype)
);

CREATE TABLE Pilot
(
	Pilot_id INT(6) AUTO_INCREMENT PRIMARY KEY,
	E_id INT(6),
	CONSTRAINT FOREIGN KEY fk_E_id(E_id)
	REFERENCES Employee(E_id),
	Qualification_id INT(6),
	CONSTRAINT FOREIGN KEY fk_Qualification_id(Qualification_id)
	REFERENCES Qualification(Qualification_id)
);

