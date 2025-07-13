import mysql.connector

class Model():
    def __init__(self, query, values, confirmation):
        #conection with database
        self.__connection = mysql.connector.connect(host = "localhost",
                                                    user = "administrador",
                                                    passwd = "admin123",
                                                    database = "KardexUPPE") 
        self.__cursor = self.__connection.cursor()
        self.__query = query 
        self.__values = values
        self.__confirmation = confirmation
    
    def command(self):
        try:
            self.__cursor.execute(self.__query, self.__values)
            if self.__confirmation == 1:
                self.__connection.commit()
            result = self.__cursor.fetchall()
            return result
        finally:
            self.__connection.close()
