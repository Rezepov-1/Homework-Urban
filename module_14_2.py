import sqlite3

connection= sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# for i in range(1, 11):
#     username = f'User{i}'
#     email = f'example{i}@gmail.com'
#     age = i * 10
#     balance = 1000
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, balance))
#
# # Обновляем balance у каждой 2-й записи, начиная с 1-й
# cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')
#
# # Удаляем каждую 3-ю запись, начиная с 1-й
# cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
#
# # Выбираем все записи, где возраст не равен 60
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
# rows = cursor.fetchall()
#
# # Вывод в консоль
# for row in rows:
#     print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

# #удаление записи с id = 6
#cursor.execute("DELETE FROM Users WHERE id = ?", ("6",))

# #подсчет общего количества записей
# cursor.execute("SELECT COUNT(*) FROM Users")
# total = cursor.fetchone()[0]
# print(total)

# #подсчет суммы всех балансов
# cursor.execute("SELECT SUM(balance) FROM Users")
# total_summ = cursor.fetchone()[0]
# print(total_summ)

#подсчет среднего баланса
cursor.execute("SELECT AVG(balance) FROM Users")
total_avg = cursor.fetchone()[0]
print(total_avg)


connection.commit()
connection.close()