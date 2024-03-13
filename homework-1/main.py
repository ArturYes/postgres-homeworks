"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


# Подключение к базе данных
conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="20031981artur")

cur = conn.cursor()

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/customers_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        row
                    )

finally:
    conn.close()

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="20031981artur")

cur = conn.cursor()

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/employees_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                        row
                    )

finally:
    conn.close()

conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="20031981artur")

cur = conn.cursor()

try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        row
                    )

finally:
    conn.close()
