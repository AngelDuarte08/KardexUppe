#Flask
from flask import Blueprint, render_template, request, session, url_for, redirect

#Models
from Models.Student import Student
from Models.Administrators import Administrators


auth_bp = Blueprint('auth_bp', __name__)
#Login
@auth_bp.route("/")
def index():

    session["user"] = ""
    session["id_user"] = ""

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
            userDB = dataDB[1]
            psswdDB = dataDB[2]
            rolDB = dataDB[3]
            
            if userLogin == userDB and psswdLogin == psswdDB:
                if rolDB == "Administrador":
                    session["user"] = userDB
                    session["id_user"] = idDB
                    return redirect(url_for("admin_bp.inicio"))
                
                elif rolDB == "Docente":
                    session["user"] = userDB
                    session["id_user"] = idDB
                    return redirect(url_for("teacher_bp.inicio"))
                
            else: 
                errorMsg = "Usuario o contraseña incorrectos"
                return render_template("auth/index.html", error = errorMsg)
                

    else:
        dataDB = resultDB[0]

        idDB = dataDB[0]
        userDB = dataDB[1]
        psswdDB = dataDB[2]

        session["user"] = userDB
        session["id_user"] = idDB
        
        if userLogin == userDB and psswdLogin == psswdDB:
            return redirect(url_for("student_bp.inicio"))
        else: 
            errorMsg = "Usuario o contraseña incorrectos"
            return render_template("auth/index.html", error = errorMsg)