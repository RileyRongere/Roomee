CREATE DATABASE IF NOT EXISTS roomee;

USE roomee;

CREATE TABLE IF NOT EXISTS users (
  user_id INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  gender VARCHAR(10)
);