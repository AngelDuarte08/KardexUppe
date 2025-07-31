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
        print(data)
        db = Model(query, data, 1)
        db.command()
