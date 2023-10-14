# MySQL Advanced Project

This project explores advanced SQL concepts and tasks related to MySQL. You will work with an Ubuntu 18.04 LTS environment and MySQL 5.7.30. The project covers topics such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers in MySQL.

## Project Structure

- All project files are located in this directory.
- SQL queries should be well-commented just before the query, following the provided syntax.
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE).
- The project files should end with a newline.

## Getting Started

To work on this project, you can use a "container-on-demand" environment running Ubuntu 18.04 with Python 3.7. You can connect to this environment via SSH or WebTerminal.

In the container, you should start the MySQL database server before using it:

```bash
$ service mysql start

Database Credentials
In the container, use the following credentials for MySQL:

Username: root
Password: root

Importing Data
You can import data into a database using SQL dumps as follows:

1. Create a new database (if not already created):
$ echo "CREATE DATABASE my_database;" | mysql -uroot -proot

1. Import data from an SQL dump into the newly created database:
$ curl "URL_TO_SQL_DUMP" -s | mysql -uroot -proot my_database

1. Query the imported data:
$ echo "SELECT * FROM table_name" | mysql -uroot -proot my_database

Project Tasks
Each SQL file in this project directory corresponds to a specific task. You will find a comment at the beginning of each file describing the task it addresses. Ensure you understand the task's requirements before executing the SQL queries.

Learning Objectives
By the end of this project, you are expected to:

Create tables with constraints.
Optimize queries by adding indexes.
Implement stored procedures and functions in MySQL.
Implement views in MySQL.
Implement triggers in MySQL.

Remember that the length of your files will be tested using wc. Ensure that your project files meet the specified requirements.

Good luck with your MySQL advanced project! If you have any questions or need assistance, feel free to reach out.


This README provides an overview of the project, instructions for setup, and guidance on how to work with the MySQL database and SQL files. It's important to keep the README well-organized and informative to help both yourself and others working on or reviewing the project.

