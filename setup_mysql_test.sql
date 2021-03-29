-- Prepare a MySQL  test server

-- Creating the database
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Creating a new user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Giving all privileges to the new user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Giving SELECT privileges to new user on 'performance_schema' database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;
