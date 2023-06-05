-- Create Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtb_0d_2;
-- Create USER
CREATE USER IF NOT EXISTS
user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANT ALL PRIVILEGES ON
*.* TO user_0d_2@localhost;
