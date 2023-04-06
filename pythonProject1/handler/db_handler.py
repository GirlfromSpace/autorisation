# подключаем SQLite
import sqlite3

def login(username, password, signal):
    con = sqlite3.connect('handler/app_database')
    cur = con.cursor()

    #Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE username="{username}";')
    value = cur.fetchall()

    if value != [] and value [0][2]==password:
        signal.emit('Успешная авторизация')
    else:
        signal.emit('Проверьте правильность ввода данных')