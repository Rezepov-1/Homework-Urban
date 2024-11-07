import sqlite3


# Функция для создания таблиц Products и Users, если они ещё не созданы
def initiate_db():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    # Создание таблицы Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL DEFAULT 1000,
    UNIQUE(username, email)  -- Ограничение уникальности на комбинацию username + email
    )
    ''')
    conn.commit()
    conn.close()


# Функция для получения всех продуктов из таблицы Products
def get_all_products():
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products


# Функция для добавления пользователя в таблицу Users
def add_user(username, email, age):
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    conn.commit()
    conn.close()


# Функция для проверки наличия пользователя в таблице Users
def is_included(username, email):
    conn = sqlite3.connect('not_telegram.db')
    cursor = conn.cursor()
    # Проверяем, существует ли пользователь с данным именем и email
    cursor.execute('SELECT * FROM Users WHERE username = ? AND email = ?', (username, email))
    result = cursor.fetchone()
    conn.close()
    return result is not None