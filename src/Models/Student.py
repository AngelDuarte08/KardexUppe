from Models.User import User #Father class
from database.connection import Model #Database 

class Student(User):
    def __init__(self):
        self.__matricula = ""
        self.__period = ""
        self.__group = ""
        self.__curp = ""
        self.__career = ""

    def auth(self, email):
        query = "SELECT correo, contrasena FROM Alumnos WHERE correo = %s"

        db = Model(query, (email,), 0)
        return db.command()
    
    def consult():
        pass

    def register():
        pass