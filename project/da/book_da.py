import mysql.connector

class BookDa:
    def connect(self,):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self,name, writer):
        self.connect()
        self.cursor.execute("INSERT INTO BOOK (name, writer) VALUES (%s,%s)",
                            [name, writer])
        self.connection.commit()
        self.disconnect()

    def edit(self,id, name, writer):
        self.connect()
        self.cursor.execute("UPDATE BOOK SET NAME=%s, WRITER=%s WHERE ID=%s",
                            [name,writer,id])
        self.connection.commit()
        self.disconnect()

    def remove(self,id):
        self.connect()
        self.cursor.execute("DELETE FROM BOOK WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK ORDER BY NAME")
        book_list = self.cursor.fetchall()
        self.disconnect()
        return book_list if book_list else None


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM BOOK WHERE ID=%s",
                            [id])
        book = self.cursor.fetchall()
        self.disconnect()
        return book[0] if book else None