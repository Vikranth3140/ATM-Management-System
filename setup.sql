-- setup.sql
CREATE DATABASE IF NOT EXISTS atm_system;
USE atm_system;

CREATE TABLE IF NOT EXISTS accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    pin VARCHAR(4) NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);