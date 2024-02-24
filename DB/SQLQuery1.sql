-- Create database:

CREATE DATABASE Advertising_management;



-- Drop database:

DROP DATABASE IF EXISTS Advertising_management;



-- Drop tables:

DROP TABLE IF EXISTS T_Advertiser
DROP TABLE IF EXISTS T_Ad



USE [Advertising_management]



-- Advertiser:

CREATE TABLE T_Advertiser (
		id				INT					PRIMARY KEY,
		clicks			INT,
		views			INT,
		name			NVARCHAR(512)
	);



-- Ad:

CREATE TABLE T_Ad (
		id				INT					PRIMARY KEY,
		clicks			INT,
		views			INT,
		title			NVARCHAR(512),
		imgUrl			NVARCHAR(512),
		link			NVARCHAR(512),
		advertiser_id   INT,
		FOREIGN KEY (advertiser_id) REFERENCES T_Advertiser (id)
);