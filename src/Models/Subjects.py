#Database
from database.connection import Model 
class Subject(): 
    def __init__(self):
        self.__name = "" 
        self.__codeCourse = "" 
        self.__numCredits = ""
        self.__numHours = ""

    def consult(self):
        pass

    def register(self, data):
        query = "INSERT INTO Materias(nombreMateria, codigoCurso, numeroCreditos, numeroHoras, cuatrimestre) VALUES(%s, %s, %s, %s, %s);"
        db = Model(query, data, 1)
        db.command()
