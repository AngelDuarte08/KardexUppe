#Flask
from flask import Blueprint, render_template, session, redirect, url_for, request, flash

#JSON
import json

#Models
from Models.Administrators import Administrators
from Models.Student import Student
from Models.Subjects import Subject

#Sql
from mysql.connector import Error

#Para datos decimales
from decimal import Decimal

#Admins
admins_bp = Blueprint('admins_bp', __name__, url_prefix='/administrador' )


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

@admins_bp.route("/")
def LogOut():
    session["id_user"] = ""
    session["rol"] = ""

    return render_template("auth/index.html")

@admins_bp.route("/Insertar_alumno", methods=['POST'])
def insert_student():

    names = request.form.get("names")
    lastnameF = request.form.get("lastname1")
    lastnameM = request.form.get("lastname2")
    curp = request.form.get("curp")
    tel = request.form.get("tel")
    street = request.form.get("street")
    num = request.form.get("number")
    cp = request.form.get("zipCode")
    colony = request.form.get("coliny")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    matricula = request.form.get("matricula")
    cuatrimestre = int(request.form.get("quarter"))
    group = request.form.get("group")
    email = request.form.get("emailInput")
    pssword = request.form.get("passwordInput")
    career = request.form.get("role")

    adress = {
        "calle": street,
        "numero": num,
        "cp": cp,
        "colonia": colony,
        "ciudad": city,
        "estado": state,
        "pais": country
    }
    adress_json = json.dumps(adress)

    dataForm = [names, lastnameF, lastnameM, adress_json, tel, email, pssword, matricula,
    cuatrimestre, group, curp, career]

    try:
        student = Student()
        student.register(dataForm)
    except Error as e:
        kind = "Error"
        message = f"Usuario no se puede registra \n{e}"
        
        return render_template("Warning/MessageStudent.html", tipo=kind, Mensage=message)
    finally: 
        kind = "Exitoso"
        message = "Usuario registrado correctamente"

        return render_template("Warning/MessageStudent.html", tipo=kind, Mensage=message)
    
@admins_bp.route("/Insertar_administrador", methods=['POST'])
def insert_admins():

    names = request.form.get("names")
    lastnameF = request.form.get("lastname1")
    lastnameM = request.form.get("lastname2")
    tel = request.form.get("tel")
    street = request.form.get("street")
    num = request.form.get("number")
    cp = request.form.get("zipCode")
    colony = request.form.get("coliny")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    email = request.form.get("emailInput")
    pssword = request.form.get("passwordInput")
    role = request.form.get("role")

    adress = {
        "calle": street,
        "numero": num,
        "cp": cp,
        "colonia": colony,
        "ciudad": city,
        "estado": state,
        "pais": country
    }
    adress_json = json.dumps(adress)

    dataForm = [names, lastnameF, lastnameM, adress_json, tel, email, pssword, role]


    try:
        admin = Administrators()
        admin.register(dataForm)

    except Error as e:
        kind = "Error"
        message = f"Usuario no eregistrado \n{e}"

        return render_template("Warning/MessageAdmins.html", tipo=kind, Mensage=message)
    
    finally:
        kind = "Exitoso"
        message = "Usuario registrado correctamente"

        return render_template("Warning/MessageAdmins.html", tipo=kind, Mensage=message)
    
@admins_bp.route("/Insertar_subject", methods=['POST'])
def insert_subject():


    names = request.form.get("name")
    code = request.form.get("code")
    creditos = float(request.form.get("credits"))
    hours = int(request.form.get("hours"))
    quarter = int(request.form.get("quarter"))

    dataForm = [names, code, creditos, hours, quarter]


    try:  
        subjects = Subject()
        subjects.register(dataForm)

    except Error as e:
        kind = "Error"
        message = f"Error al invocar register(): {e}"

        return render_template("Warning/MessageSubjects.html", tipo=kind, Mensage=message)
    
    finally:
        kind = "Exitoso"
        message = "Usuario registrado correctamente"

        return render_template("Warning/MessageSubjects.html", tipo=kind, Mensage=message)
    
@admins_bp.route("/Buscar_alumno")
def serch_student():
    try: 
        student = Student()
        table = student.consultTable()

        fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo', 'matricula', 'cuatrimestre', 'grupo', 'carrera']
        dictinaryList =[
            dict(zip(fields, fila))
            for fila in table
            ]
        

        return render_template('Admins/SerchStudent.html',
                               datos=dictinaryList)
    except Error as e:
        kind = "Error"
        message = f"Error al invocar register(): {e}"

        return render_template("Warning/MessageSubjects.html", tipo=kind, Mensage=message)
    
@admins_bp.route("/Buscar_materia")
def serch_subject():
    try: 
        subject = Subject()
        table = subject.consultTable()

        dictinaryList = [
            {
                'nombre': fila[0],
                'codigo': fila[1],
                'credito': float(fila[2]) if isinstance(fila[2], Decimal) else fila[2],
                'horas': fila[3]
            }
            for fila in table
        ]

        return render_template('Admins/SerchSubject.html',
                               datos=dictinaryList)
    except Error as e:
        kind = "Error"
        message = f"Error al invocar register(): {e}"

        return render_template("Warning/MessageSubjects.html", tipo=kind, Mensage=message)

@admins_bp.route("/Buscar_empleado")
def serch_staf():
    try: 
        admin = Administrators()
        table = admin.consultTable()

        fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo', 'rol']
        dictinaryList =[
            dict(zip(fields, fila))
            for fila in table
            ]

        return render_template('Admins/SerchStaf.html',
                               datos=dictinaryList)
    except Error as e:
        kind = "Error"
        message = f"Error al invocar register(): {e}"

        return render_template("Warning/MessageSubjects.html", tipo=kind, Mensage=message)
    
@admins_bp.route("/Buscar_un_empleado", methods=["POST"])
def serch_one_staf():
    email = request.form["email"]

    if not email:
        return redirect(url_for("admins_bp.serch_staf"))
    else:
        try: 
            admin = Administrators()
            table = admin.consultOne(email)
            fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo', 'rol']
            dictinaryList =[
                dict(zip(fields, fila))
                for fila in table
                ]

            if table:
                return render_template('Admins/SerchStaf.html',
                               datos=dictinaryList)
            else:
                flash("Empleado no encontrado", "error-message")
                return redirect(url_for("admins_bp.serch_staf"))

        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "error-message")
            return redirect(url_for("admins_bp.serch_staf"))
        
@admins_bp.route("/Buscar_un_alumno", methods=["POST"])
def serch_one_student():
    matricula = request.form["matricula"]

    if not matricula:
        return redirect(url_for("admins_bp.serch_student"))
    else:
        try: 
            student = Student()
            table = student.consultOne(matricula)
            fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo', 'matricula', 'cuatrimestre', 'grupo', 'carrera']
            dictinaryList =[
                dict(zip(fields, fila))
                for fila in table
                ]

            if table:
                return render_template('Admins/SerchStudent.html',
                               datos=dictinaryList)
            else:
                flash("Alumno no encontrado", "error-message")
                return redirect(url_for("admins_bp.serch_student"))

        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "error-message")
            return redirect(url_for("admins_bp.serch_student"))
        

@admins_bp.route("/Buscar_una_materia", methods=["POST"])
def serch_one_subject():
    code = request.form["code"]

    if not code:
        return redirect(url_for("admins_bp.serch_subject"))
    else:
        try: 
            subject = Subject()
            table = subject.consultOne(code)

            dictinaryList = [
                {
                    'nombre': fila[0],
                    'codigo': fila[1],
                    'credito': float(fila[2]) if isinstance(fila[2], Decimal) else fila[2],
                    'horas': fila[3]
                }
                for fila in table
            ]

            if table:
                return render_template('Admins/SerchSubject.html',
                                datos=dictinaryList)
            else:
                flash("Materia no encontrado", "error-message")
                return redirect(url_for("admins_bp.serch_subject"))

        except Exception as e:
            flash(f"Ocurrió un error: {str(e)}", "error-message")
            return redirect(url_for("admins_bp.serch_subject"))