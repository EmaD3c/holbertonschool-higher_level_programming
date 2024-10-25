-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the table 'states.
CREATE TABLE IF NOT EXISTS states (
    id INT UNIQUE DEFAULT 1 NOT NULL,
    name VARCHAR(256) NOT NULL
);
