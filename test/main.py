import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

connection = sqlite3.connect('budget_db.sqlite3')

cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS
purchases(purchases_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT,
FOREIGN KEY(store_id) REFERENCES stores(store_id))"""

cursor.execute(command2)

cursor.execute("INSERT INTO stores (store_id, location) VALUES (21, 'New York')")
cursor.execute("INSERT INTO stores (store_id, location) VALUES (95, 'Los Angeles')")
cursor.execute("INSERT INTO stores (store_id, location) VALUES (64, 'Chicago')")

cursor.execute("INSERT INTO purchases (store_id, total_cost) VALUES (1, 100.50)")
cursor.execute("INSERT INTO purchases (store_id, total_cost) VALUES (2, 200.50)")

cursor.execute("INSERT INTO purchases VALUES (5, 3, 150.75)")
cursor.execute("INSERT INTO purchases VALUES (6, 1, 300.00)")

cursor.execute("SELECT * FROM purchases")

results = cursor.fetchall()

print(results)