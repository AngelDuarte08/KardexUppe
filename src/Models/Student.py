from Models.User import User #Father class
from database.connection import Model #Database 

from flask import request

class Student(User):
    def __init__(self):
        self.__matricula = ""
        self.__period = ""
        self.__group = ""
        self.__curp = ""
        self.__career = ""

    def auth(self, email, password):
        try:
            self.__user = email
            self.__password = password

            data = [self.__user, self.__password] 

            query = "SELECT idAlumno, correo, contrasena FROM Alumnos WHERE correo = %s AND contrasena = %s;"

            db = Model(query, data, 0)
            resultDB = db.command()
        except: 
            resultDB = None
        finally: 
            return resultDB 
        
    def credential(self, idUser):
        self.__idUser = idUser
        data = [self.__idUser]

        query = "SELECT nombres , apellidoP, apellidoM, matricula, cuatrimestre, grupo, carrera, correo FROM Alumnos WHERE idAlumno = %s;"
        db = Model(query, data, 0)
        dataCredential = db.command()

        return dataCredential[0]

    def register():
        pass