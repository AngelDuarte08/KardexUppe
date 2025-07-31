#Flask
from flask import Blueprint, render_template, session, redirect, url_for, request

#Models
from Models.Student import Student

#Collections
from collections import defaultdict


#Students
student_bp = Blueprint('student_bp', __name__, url_prefix='/alumnos')

@student_bp.route("/inicio")
def inicio():
    student = Student()

    idUser = session.get("id_user")
    resultDB = student.credential(idUser)
    
    if not resultDB:
        return redirect(url_for("auth_bp.index"))
    else: 
        names = resultDB[0]
        lastnameF = resultDB[1]
        lastnameM = resultDB[2]
        matricula = resultDB[3]
        fortMonth = resultDB[4]
        group = resultDB[5]
        career = resultDB[6]
        email = resultDB[7]

        return render_template("Students/StartStudents.html", 
                            nombres=names, 
                            apellidoP=lastnameF,
                            apellidoM= lastnameM,
                            matricula=matricula,
                            carrera=career,
                            cuatrimestre=fortMonth,
                            grupo=group,
                            correo=email )


@student_bp.route("/Kardex")
def Kardex():
    student = Student()

    matricula = session.get("matricula")
    resultDB = student.kardex(matricula)

    subjectsPerCuatri = defaultdict(list)
    for subject in resultDB:
        cuatri =  subject[6]
        subjectsPerCuatri[cuatri].append(subject)

    return render_template("Students/Kardex.html", materiasPorCuatri=subjectsPerCuatri)


@student_bp.route("/")
def LogOut():

    session["id_user"] = ""
    session["matricula"] = ""
    return render_template("auth/index.html")
