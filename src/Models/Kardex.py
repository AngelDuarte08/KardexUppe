#Database
from database.connection import Model 


class Kardex(): 
    def __init__(self):
        self.__matricula = "" 
        self.__codeCourse = "" 
        self.__idAdmin = ""
        self.__qualification = ""
        self.__status = ""

    def register(self, data):
        query = "INSERT INTO Kardex(matricula, codigoCurso, idAdmin, calificacion, estatus) VALUES(%s, %s, %s, %s, %s);"
        db = Model(query, data, 1)
        db.command()

    