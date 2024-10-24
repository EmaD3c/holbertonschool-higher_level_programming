-- Create the user 'user_0d_1' with password 'user_0d_1_pwd'
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd'

-- Grant all privileges on all databases to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes (to make the grant effective)
FLUSH PRIVILEGES;
