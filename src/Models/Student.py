from src.Models.User import User

class Student(User):
    def __init__(self, matricula, period, group, curp, career):
        self.__matricula = matricula
        self.__period = period
        self.__group = group
        self.__curp = curp
        self.__career = career
    
    def consult():
        pass

    def register():
        pass