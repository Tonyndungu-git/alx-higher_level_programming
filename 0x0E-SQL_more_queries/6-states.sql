-- create database and use it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- create table that auto-generates id
CREATE TABLE IF NOT EXISTS
states(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);
