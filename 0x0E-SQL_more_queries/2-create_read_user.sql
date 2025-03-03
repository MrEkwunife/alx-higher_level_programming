-- create a database and give user select access to it
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates a user with Select access
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2 TO user_0d_2'@'localhost';
FLUSH PRIVILEGES;
