-- Create the database 'hbtn_0d_usa' if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database 'hbtn_0d_usa'
USE hbtn_0d_usa;

-- Create the table 'cities'
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL, -- Foreign key column
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) -- Foreign key
);
