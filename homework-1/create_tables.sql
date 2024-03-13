-- SQL-команды для создания таблиц
CREATE TABLE customers
(
    customer_id serial PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees
(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL,
    notes text
);

CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id serial REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL
);
