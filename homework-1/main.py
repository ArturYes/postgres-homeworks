"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


def insert_data(table_name):
    conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="20031981artur")
    conn.cursor()
    try:
        with conn:
            with conn.cursor() as cursor:
                with open(f'north_data/{table_name}_data.csv', 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in reader:
                        cursor.execute(
                            f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})",
                            row
                        )
    finally:
        conn.close()


tables = {
    'customers': ('customer_id, company_name, contact_name',),
    'employees': ('employee_id, last_name, first_name, hire_date, address, city',),
    'orders': ('order_id, order_date, customer_id, employee_id, total',),
}

for table, columns in tables.items():
    insert_data(table)
