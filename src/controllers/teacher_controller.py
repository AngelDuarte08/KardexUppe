#Flask
from flask import Blueprint, render_template, session, redirect, url_for, request, flash

#Model
from Models.Administrators import Administrators
from Models.Subjects import Subject
from Models.Student import Student
from Models.Kardex import Kardex
#Pandas
import pandas as pd

#Json
import json

#Traceback
import traceback

teacher_bp = Blueprint('teacher_bp', __name__, url_prefix='/Docente')

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

@teacher_bp.route("/Registar_calificaciones")
def record_grades():
    return render_template("Teachers/Qualifications.html")


@teacher_bp.route("/Verificacion", methods=['POST'])
def excel():
    excelFile = request.files.get('excelFile')

    if not excelFile or excelFile.filename == '':
        flash("No se recibió ningún archivo.")
        return redirect(url_for('teacher_bp.record_grades'))

    try:
        # Código de la clase
        df_code = pd.read_excel(excelFile, nrows=1, header=None, engine='openpyxl')
        classCode = df_code.iloc[0, 1]

        # Datos de calificaciones
        df = pd.read_excel(excelFile, skiprows=1, engine='openpyxl')
        df.columns = df.columns.str.strip().str.lower()  # Elimina espacios y los combierte a minusculas
        df['codigo'] = classCode

        # Lista de matrículas
        matriculas = df['matricula'].tolist()  # ojo con la M mayúscula

        # Consultar nombres en la BD
        student = Student()
        studentName = student.serch(matriculas)

        mapName = {
            row[0]: f"{row[1]} {row[2]} {row[3]}"
            for row in studentName
        }

        # Agregar columna de nombre completo
        df['matricula'] = df['matricula'].astype(str).str.strip()
        df['nombre_completo'] = df['matricula'].map(mapName)


        # Datos del maestro
        idUser = session.get("id_user")
        teacher = Administrators()
        teacherName = teacher.serch(idUser)

        # Pasar a diccionario
        dictionaryList = df.to_dict(orient='records')

        # Nombre de la materia
        subject = Subject()
        className = subject.serch(classCode)

        return render_template(
            "Teachers/Check.html",
            Materia=className,
            nombreD=teacherName[0],
            apellidoPD=teacherName[1],
            apellidoMD=teacherName[2], 
            Codigo=classCode,
            datos=dictionaryList
        )

    except Exception as e:
        print("Error al procesar el archivo:", e)
        traceback.print_exc()
        flash(f"Error al procesar el archivo: {str(e)}")
        return redirect(url_for('teacher_bp.record_grades'))


@teacher_bp.route("/Confirmacion", methods=['POST'])
def registerKardex():
    try:
        dataJson = request.form.get('datos')
        print("Contenido recibido:", dataJson)
        if not dataJson:
            flash("No se recibieron datos para guardar.")
            return redirect(url_for('teacher_bp.record_grades'))
        
        datos = json.loads(dataJson)
        print("JSON recibido:", dataJson)
        idAdmin = session.get("id_user")

        kardex = Kardex()

        for registro in datos:
            data = (
                registro['matricula'],
                registro['codigo'],
                idAdmin,
                registro['calificacion'],
                registro['estatus']
            )
            kardex.register(data)

        flash("Datos guardados exitosamente en el Kardex.")
        return redirect(url_for('teacher_bp.record_grades'))       
    except Exception as e:
        print("Error al guardar en Kardex:", e)
        traceback.print_exc()
        flash(f"Error al guardar en Kardex: {str(e)}")
        return redirect(url_for('teacher_bp.record_grades'))
        

@teacher_bp.route("/")
def LogOut():
    session["id_user"] = ""
    session["rol"] = ""

    return render_template("auth/index.html")