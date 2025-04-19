from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Ingresar/Actualizar')


class RegistroForm(FlaskForm):
    apellido = StringField('Apellido', validators=[DataRequired()])
    nombre = StringField('Nombre', validators=[DataRequired()])
    dni = StringField('DNI', validators=[DataRequired()])
    fnacto = DateField('Fecha de Nacimiento')
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Ingresar/Actualizar')
    
class AnioForm(FlaskForm):
	numero = StringField('Numero', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class CargoDocenteForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class CicloLectivoForm(FlaskForm):
	anio = IntegerField('Anio', validators=[DataRequired()])
	finicio = DateField('Finicio', validators=[DataRequired()])
	ffin = DateField('Ffin', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class InstitucionForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	domicilio = StringField('Domicilio', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class MateriaForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class PersonaForm(FlaskForm):
	apellido = StringField('Apellido', validators=[DataRequired()])
	nombre = StringField('Nombre', validators=[DataRequired()])
	dni = IntegerField('Dni', validators=[DataRequired()])
	fnacto = DateField('Fnacto', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class TipoContactoForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class TurnoForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class ContactoPersonaForm(FlaskForm):
	persona_id = IntegerField('Persona_Id', validators=[DataRequired()])
	tipocontacto_id = IntegerField('Tipocontacto_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class DocenteForm(FlaskForm):
	legajo = IntegerField('Legajo', validators=[DataRequired()])
	persona_id = IntegerField('Persona_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class UsuarioForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	password_hash = StringField('Password_Hash', validators=[DataRequired()])
	persona_id = IntegerField('Persona_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class DocenteCargoForm(FlaskForm):
	docente_id = IntegerField('Docente_Id', validators=[DataRequired()])
	cargodocente_id = IntegerField('Cargodocente_Id', validators=[DataRequired()])
	finicio = DateField('Finicio', validators=[DataRequired()])
	ffin = DateField('Ffin', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class PosteoForm(FlaskForm):
	texto = StringField('Texto', validators=[DataRequired()])
	fecha = DateField('Fecha', validators=[DataRequired()])
	usuario_id = IntegerField('Usuario_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class AlumnoForm(FlaskForm):
	legajo = IntegerField('Legajo', validators=[DataRequired()])
	persona_id = IntegerField('Persona_Id', validators=[DataRequired()])
	fingreso = DateField('Fingreso', validators=[DataRequired()])
	fegreso = DateField('Fegreso', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class AlumnoComisionForm(FlaskForm):
	comision_id = IntegerField('Comision_Id', validators=[DataRequired()])
	alumno_id = IntegerField('Alumno_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class CarreraForm(FlaskForm):
	institucion_id = IntegerField('Institucion_Id', validators=[DataRequired()])
	nombre = StringField('Nombre', validators=[DataRequired()])
	anios = IntegerField('Anios', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class ComisionForm(FlaskForm):
	ciclolectivo_id = IntegerField('Ciclolectivo_Id', validators=[DataRequired()])
	cuatrimestre_id = IntegerField('Cuatrimestre_Id', validators=[DataRequired()])
	turno_id = IntegerField('Turno_Id', validators=[DataRequired()])
	materiadocente_id = IntegerField('Materiadocente_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class CuatrimestreForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	ciclolectivo_id = IntegerField('Ciclolectivo_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class MateriaDocenteForm(FlaskForm):
	docente_id = IntegerField('Docente_Id', validators=[DataRequired()])
	materiaplan_id = IntegerField('Materiaplan_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class MateriaPlanForm(FlaskForm):
	planestudio_id = IntegerField('Planestudio_Id', validators=[DataRequired()])
	materia_id = IntegerField('Materia_Id', validators=[DataRequired()])
	anio_id = IntegerField('Anio_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')

class PlanEstudioForm(FlaskForm):
	nombre = StringField('Nombre', validators=[DataRequired()])
	finicio = DateField('Finicio', validators=[DataRequired()])
	ffin = DateField('Ffin', validators=[DataRequired()])
	carrera_id = IntegerField('Carrera_Id', validators=[DataRequired()])
	submit = SubmitField('Ingresar/Actualizar')
	
