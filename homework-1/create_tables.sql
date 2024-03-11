-- SQL-команды для создания таблиц
CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    employee_id INT,
    order_date DATE,
    ship_city VARCHAR(255),
    author INT
);

CREATE TABLE customers
(
    customer_id INT PRIMARY KEY,
    company_name VARCHAR(255),
    contact_name VARCHAR(255),
    author INT,
    FOREIGN KEY (author) REFERENCES orders (order_id)
);

CREATE TABLE employees
(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    title VARCHAR(255),
    birth_date DATE,
    notes VARCHAR(255),
    author INT,
    FOREIGN KEY (author) REFERENCES orders (order_id)
);
