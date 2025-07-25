#Flask
from flask import Blueprint, render_template, session, redirect, url_for

#Model
from Models.Administrators import Administrators

teacher_bp = Blueprint('teacher_bp', __name__, url_prefix='/docente')

#Teachers
@teacher_bp.route("/inicio")
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
    return render_template("Teachers/StartTeachers.html",
                           nombre=names,
                           apellidoP=lastnameF,
                           apellidoM=lastnameM,
                           tel=tel,
                           rol=rol,
                           correo =correo)
