import sqlite3
import pandas as pd
import os

DATABASE_NAME = 'financial_budget.db'

def database_setup():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    