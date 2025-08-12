#Models
from Models.User import User #Father class
from database.connection import Model #Database 

#Flask
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

            query = "SELECT idAlumno, matricula FROM Alumnos WHERE correo = %s AND contrasena = %s;"

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
    
    def kardex(self, matricula):
        self.__matricula = matricula
        data = [self.__matricula]

        query = "SELECT * FROM kardexvista WHERE matricula = %s;"
        db = Model(query, data, 0)
        result = db.command()
        return result


    def register(self, data):
        query= "INSERT INTO Alumnos(nombres, apellidoP, apellidoM, direccion, telefono, correo, contrasena, matricula, cuatrimestre, grupo, curp, carrera) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);" 
        db = Model(query, data, 1)
        db.command()

    def serch(self, matriculas):
        placeholders = ', '.join(['%s'] * len(matriculas))

        query = f"SELECT matricula, nombres, apellidoP, apellidoM FROM Alumnos WHERE matricula IN ({placeholders});"
        db = Model(query, matriculas, 0)
        result = db.command()
        return result