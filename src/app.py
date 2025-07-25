#Flask
from flask import Flask

#Controller
from controllers.auth_controller import auth_bp
from controllers.student_controller import student_bp
from controllers.teacher_controller import teacher_bp
from controllers.administrator_controller import admins_bp

app = Flask(__name__)
app.secret_key = "AngelDios112002"

app.register_blueprint(auth_bp)
app.register_blueprint(student_bp)
app.register_blueprint(teacher_bp)
app.register_blueprint(admins_bp)

if __name__ == '__main__':
    app.run(debug=True)
