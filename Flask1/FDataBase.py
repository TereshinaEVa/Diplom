import sqlite3

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()


    def getUsers(self):
        users_ = '''SELECT * FROM users'''
        try:
            self.__cur.execute(users_)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print('Ошибка чтения из БД')
        return []

    def addPost(self, username, password, ege, grade):
        try:
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?,?,?,?)", (username, password, ege, grade))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка регистрации пользователя' + str(e))
            return False
        return True

