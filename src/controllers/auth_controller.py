#Flask
from flask import Blueprint, render_template, request, session, url_for, redirect

#Models
from Models.Student import Student
from Models.Administrators import Administrators


auth_bp = Blueprint('auth_bp', __name__)
#Login
@auth_bp.route("/")
def index():

    session["id_user"] = ""
    session["matricula"] = ""
    session["rol"] = ""

    return render_template("auth/index.html")

@auth_bp.route("/index.html", methods=['POST'])
def auth(): 
    userLogin = request.form['email']
    psswdLogin = request.form['password']

    student = Student()
    resultDB = student.auth(userLogin, psswdLogin)



    if not resultDB: 
        administrators = Administrators()
        resultDB = administrators.auth(userLogin, psswdLogin)
        if  not resultDB:
            errorMsg = "Usuario no encontrado"
            return render_template("auth/index.html", error = errorMsg)
        else:
            dataDB = resultDB[0]

            idDB = dataDB[0]
            rolDB = dataDB[1]
            
            if rolDB == "Administrador":
                session["id_user"] = idDB
                session["rol"] = rolDB
                return redirect(url_for("admin_bp.inicio"))
            
            elif rolDB == "Docente":
                session["id_user"] = idDB
                session["rol"] = rolDB
                return redirect(url_for("teacher_bp.inicio"))
    else:
        dataDB = resultDB[0]

        idDB = dataDB[0]
        matricula= dataDB[1]

        session["id_user"] = idDB
        session["matricula"] = matricula
        return redirect(url_for("student_bp.inicio"))