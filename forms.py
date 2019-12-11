from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length

class RegistroForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    email = StringField('Correo electrónico', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    slug = StringField('Slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Guardar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Acceder')