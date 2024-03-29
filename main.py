from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.route('/', methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if (request.method == 'POST'):
        alum = Alumnos(nombre=create_form.nombre.data,
                       apaterno=create_form.apaterno.data, email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
    return render_template('index.html', form=create_form)


@app.route('/ABCompleto', methods=['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)
    students = Alumnos.query.all()

    return render_template('ABCompleto.html', form=create_form, alumnos=students)


@app.route('/modificar', methods=['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if (request.method == 'GET'):
        id = request.args.get('id')
        student = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = student.nombre
        create_form.apaterno.data = student.apaterno
        create_form.email.data = student.email

    if (request.method == 'POST'):
        id = create_form.id.data
        studen = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        studen.nombre = create_form.nombre.data
        studen.apaterno = create_form.apaterno.data
        studen.email = create_form.email.data
        db.session.add(studen)
        db.session.commit()
        return redirect(url_for('ABCompleto'))

    return render_template('modificar.html', form=create_form)


@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if(request.method == 'GET'):
        id = request.args.get('id')
        student = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = student.nombre
        create_form.apaterno.data = student.apaterno
        create_form.email.data = student.email
    if(request.method == 'POST'):
        id = create_form.id.data
        studen = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        studen.nombre = create_form.nombre.data
        studen.apaterno = create_form.apaterno.data
        studen.email = create_form.email.data
        db.session.delete(studen)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    
    return render_template('eliminar.html', form = create_form)


if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
