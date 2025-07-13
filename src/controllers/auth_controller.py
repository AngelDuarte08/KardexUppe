from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from Models.Student import Student
from Models.Administrators import Administrators

auth_bp = Blueprint('auth_bp', __name__, template_folder='../Templates/auth')

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        pssword = request.form['password']

        student = Student()
        result = student.auth(email)

        if not result:
            admin = Administrators()
            result = admin.auth(email)
            # row = result[0]
            dbEmail = result[0]
            dbPssword = result[1]
            dbRol = result[2]

            if dbEmail == email and dbPssword == pssword:
                if dbRol == "Administrador":
                        return redirect(url_for('admin_bp.dashboard'))
                elif dbRol == "Docente": 
                    return redirect(url_for('teachers_bp.panel'))
            else:
                flash('Correo o contraseña incorrectos', 'danger')
        else:
            row = result[0]
            dbEmail = row[0]
            dbPssword = row[1] 
            if dbEmail == email and dbPssword == pssword:
                return redirect(url_for('teacher_bp.panel'))  
            else:
                flash('Correo o contraseña incorrectos', 'danger')

    return render_template('auth/index.html')
