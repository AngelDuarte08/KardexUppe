#Flask
from flask import Blueprint, render_template, session, redirect, url_for

#Models
from Models.Administrators import Administrators

#Admins
admins_bp = Blueprint('admin_bp', __name__, url_prefix='/administrador' )


@admins_bp.route("/inicio")
def inicio():
    admin = Administrators()

    idUser = session.get("id_user")
    resultDB = admin.credential(idUser)
    
    if not resultDB:
        return redirect(url_for("auth_bp.index"))
    else: 
        names = resultDB[0]
        lastnameF = resultDB[1]
        lastnameM = resultDB[2]
        tel = resultDB[3]
        rol = resultDB[4]
        correo = resultDB[5]

    return render_template("Admins/StartstudentAdmin.html",
                           nombre=names,
                           apellidoP=lastnameF,
                           apellidoM=lastnameM,
                           tel=tel,
                           rol=rol,
                           correo = correo)

@admins_bp.route("/Registrar_usuario")
def registerU():
    return render_template("Admins/RegisterUsers.html")

@admins_bp.route("/Registrar_alumno")
def registerS():
    return render_template("Admins/RegisterStudents.html")

@admins_bp.route("/Registrar_materia")
def registerM():
    return render_template("Admins/RegisterSubject.html")