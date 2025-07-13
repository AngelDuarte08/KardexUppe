from Models.User import User #Father class
from database.connection import Model #Database 

class Administrators(User): 
    def __init__(self,):
        self.__rol = "" 
        self.__estatus = ""

    def auth(self, email):
        query = "SELECT correo contrasena rol FROM Admins WHERE correo = %s"

        db = Model(query, (email,), 0)
        return db.command()
    
    def consult(self):
        pass

    def register():
        pass