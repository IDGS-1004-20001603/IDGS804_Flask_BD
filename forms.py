from wtforms import Form, StringField, IntegerField, EmailField, validators

class UserForm(Form):
    id = IntegerField('id', [
        validators.number_range(min = 1, max = 20, message = 'Valor no valido')
    ])
    nombre = StringField('nombre', [
        validators.DataRequired(message = 'El campo requiere de un valor')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message = 'El campo requiere de un valor')
    ])
    email = EmailField('correo', [
        validators.DataRequired(message = 'El campo requiere de un valor'),
        validators.Email(message = 'Ingresa un correo valido')
    ])
