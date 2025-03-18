CREATE DATABASE IF NOT EXISTS blood_donation_db;

USE blood_donation_db;

CREATE TABLE IF NOT EXISTS Donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_name VARCHAR(100) NOT NULL,
    blood_group VARCHAR(5) NOT NULL,
    location VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS Requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    blood_group_needed VARCHAR(5) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS BloodAvailable (
    blood_id INT AUTO_INCREMENT PRIMARY KEY,
    blood_group VARCHAR(5) NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Emails (
    email_id INT AUTO_INCREMENT PRIMARY KEY,
    recipient_email VARCHAR(100) NOT NULL,
    subject VARCHAR(200) NOT NULL,
    body TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);