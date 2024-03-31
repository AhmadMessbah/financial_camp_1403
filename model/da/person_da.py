import mysql.connector

class PersonDa:
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

    def save(self,name, family):
        self.connect()
        self.cursor.execute("INSERT INTO __person__ (name, family) VALUES (%s,%s); CALL acc.sp_Insert_person_in_pusers_nf();",
                            [name, family])
        self.connection.commit()
        self.disconnect()

    def edit(self,id, name, family):
        self.connect()
        self.cursor.execute("UPDATE __person__ SET name=%s, family=%s WHERE ID=%s",
                            [name,family,id])
        self.connection.commit()
        self.disconnect()

    def remove(self,id):
        self.connect()
        self.cursor.execute("DELETE FROM __person__ WHERE id=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM __person__ ORDER BY FAMILY")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list if person_list else None


    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM __person__ WHERE ID=%s",
                            [id])
        person = self.cursor.fetchall()
        self.disconnect()
        return person[0] if person else None