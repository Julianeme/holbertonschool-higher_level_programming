--script that lists all privileges of the MySQL
-- users user_0d_1 and user_0d_2 on your server (in localhost).
CREATE IF NOT EXISTS USER 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';