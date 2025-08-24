#Father class
from Models.User import User 

#Database
from database.connection import Model  

class Administrators(User): 
    def __init__(self,):
        self.__rol = "" 
        self.__estatus = ""

    def auth(self, email, password):
        try: 
            self.__user = email
            self.__password = password

            data = [self.__user, self.__password]

            query = "SELECT idAdmin, rol FROM Admins WHERE correo = %s AND contrasena = %s;"

            db = Model(query, data, 0)
            resultDB = db.command()
        except:
            resultDB = None
        finally:
            return resultDB
    
    def credential(self, idUser):
        self.__idUser = idUser
        data = [self.__idUser]

        query = "SELECT nombres , apellidoP, apellidoM, telefono, rol, correo FROM Admins WHERE idAdmin = %s;"
        db = Model(query, data, 0)
        dataCredential = db.command()

        return dataCredential[0]

        

    def register(self, data):
        query= "INSERT INTO Admins(nombres, apellidoP, apellidoM, direccion, telefono, correo, contrasena, rol) VALUES(%s, %s, %s, %s, %s, %s, %s, %s);" 
        db = Model(query, data, 1)
        db.command()

    def serch(self,idUser):
        self.__data = [idUser]
        query = "SELECT nombres, apellidoP, apellidoM FROM Admins WHERE idAdmin = %s"
        db = Model(query, self.__data, 0)
        result = db.command()
        return result[0]
    
    def consultTable(self):
        query = "SELECT nombres, apellidoP, apellidoM, telefono, correo, rol FROM Admins"

        db = Model(query, "", 0)
        result = db.command()
        return result
    
    def consultOne(self, email):
        self.__data = [email]
        query = "SELECT nombres, apellidoP, apellidoM, telefono, correo, rol FROM Admins WHERE correo = %s"

        db = Model(query, self.__data, 0)
        result = db.command()
        return result