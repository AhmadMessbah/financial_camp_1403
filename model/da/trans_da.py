import mysql.connector

class TransDa:
    def connect(self):

        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="acc"
        )
        self.cursor = self.connection.cursor()

    
    
    def disconnect(self):

        self.cursor.close()
        self.connection.close()


def save(self, pid, date_time, amount, type):

    self.connect()
    self.cursor.execute(
        "INSERT INTO __transaction__ (pid ,datetime, amount , type) VALUES (%s,%s,%s,%s);",
        [pid,date_time,amount,type])
    self.connection.commit()
    self.disconnect()
    
    
    def edit(self,id, date_time, amount):
        self.connect()
        self.cursor.execute("UPDATE __transaction__ SET datetime=%s, amount=%s , amount=%s WHERE id=%s",
                            [date_time, amount, id])
        self.connection.commit()
        self.disconnect()
    
    
    def remove(self,id):
        self.connect()
        self.cursor.execute("DELETE from __transaction__  WHERE ID=%s;" ,
                            [id])
        self.connection.commit()
        self.disconnect()
    
    
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM __transaction__ ORDER BY FAMILY")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list if person_list else None


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM __transaction__ WHERE ID=%s",
                            [id])
        person = self.cursor.fetchall()
        self.disconnect()
        return person[0] if person else None