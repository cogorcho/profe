from datetime import datetime
from app import db, login
import typing
from flask_login import UserMixin
from dataclasses import dataclass
import inspect

class Util():
    def __repr__(o) -> str:
        return f"{o.to_dict()}"
    def to_dict(o):
        return {field.name:getattr(o, field.name) for field in o.__table__.c}

class Institucion(Util,db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(256), index=True, unique=True, nullable=False)
    domicilio = db.Column(db.String(256),nullable=False)

class Carrera(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('institucion_id', 'nombre', name='uix_carrera_institucion'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    institucion_id = db.Column(db.Integer(), db.ForeignKey(Institucion.id), nullable=False)
    nombre = db.Column(db.String(64), index=True, nullable=False)
    anios = db.Column(db.Integer(), nullable=False, default=0)

class CicloLectivo(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    anio = db.Column(db.Integer(), index=True, unique=True, nullable=False)
    finicio = db.Column(db.DateTime, default=datetime.now().date().replace(month=1, day=1), nullable=False)
    ffin = db.Column(db.DateTime, default=datetime.now().date().replace(month=12, day=31), nullable=False)

class Cuatrimestre(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('ciclolectivo_id', 'nombre', name='uix_cuatrimestre_ciclo'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)
    ciclolectivo_id = db.Column(db.Integer(), db.ForeignKey(CicloLectivo.id), nullable=False)

class Turno(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)

class Materia(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)

class PlanEstudio(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('carrera_id', 'nombre', name='uix_plan_carrera'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)
    finicio = db.Column(db.DateTime)
    ffin = db.Column(db.DateTime)
    carrera_id = db.Column(db.Integer(), db.ForeignKey(Carrera.id), nullable=False)

class Anio(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    numero = db.Column(db.String(64), index=True, unique=True, nullable=False)

class MateriaPlan(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('planestudio_id', 'materia_id', 'anio_id', name='uix_materia_plan'),
    )    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    planestudio_id = db.Column(db.Integer(), db.ForeignKey(PlanEstudio.id), nullable=False)
    materia_id = db.Column(db.Integer(), db.ForeignKey(Materia.id), nullable=False)
    anio_id = db.Column(db.Integer(), db.ForeignKey(Anio.id), nullable=False)

class Persona(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    apellido = db.Column(db.String(64), index=True, nullable=False)
    nombre = db.Column(db.String(64), index=True, nullable=False)
    dni = db.Column(db.Integer(), index=True, unique=True, nullable=False)
    fnacto = db.Column(db.DateTime, nullable=False)

class CargoDocente(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, nullable=False)

class Docente(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    legajo = db.Column(db.Integer(), nullable=False, default=0)
    persona_id = db.Column(db.Integer(), db.ForeignKey(Persona.id), nullable=False)
    
class vdocente(Util, db.Model):
    docente_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    legajo = db.Column(db.Integer(), nullable=False, default=0)
    apellido = db.Column(db.String(64), index=True, nullable=False)
    nombre = db.Column(db.String(64), index=True, nullable=False)
    dni = db.Column(db.Integer(), index=True, unique=True, nullable=False)

class DocenteCargo(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    docente_id = db.Column(db.Integer(), db.ForeignKey(Docente.id),nullable=False)
    cargodocente_id = db.Column(db.Integer(), db.ForeignKey(CargoDocente.id),nullable=False)
    finicio = db.Column(db.DateTime, nullable=False)
    ffin = db.Column(db.DateTime)

class MateriaDocente(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('docente_id', 'materiaplan_id', name='uix_materia_docente'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    docente_id = db.Column(db.Integer(), db.ForeignKey(Docente.id), nullable=False)
    materiaplan_id = db.Column(db.Integer(), db.ForeignKey(MateriaPlan.id), nullable=False)

class Comision(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('ciclolectivo_id', 'cuatrimestre_id', 'turno_id', 'materiadocente_id' ,name='uix_comision'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    ciclolectivo_id = db.Column(db.Integer(), db.ForeignKey(CicloLectivo.id), nullable=False)
    cuatrimestre_id = db.Column(db.Integer(), db.ForeignKey(Cuatrimestre.id), nullable=False)
    turno_id = db.Column(db.Integer(), db.ForeignKey(Turno.id), nullable=False)
    materiadocente_id = db.Column(db.Integer(), db.ForeignKey(MateriaDocente.id),nullable=False)

class Alumno(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('legajo', 'persona_id', name='uix_alumno'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    legajo = db.Column(db.Integer(), nullable=False, default=0)
    persona_id = db.Column(db.Integer(), db.ForeignKey(Persona.id), nullable=False)
    fingreso = db.Column(db.DateTime, nullable=False)
    fegreso = db.Column(db.DateTime)

class AlumnoComision(Util, db.Model):
    __table_args__ = (
        db.UniqueConstraint('comision_id', 'alumno_id', name='uix_alumno_comision'),
    )
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    comision_id = db.Column(db.Integer(), db.ForeignKey(Comision.id), nullable=False)
    alumno_id = db.Column(db.Integer(), db.ForeignKey(Alumno.id), nullable=False)

class TipoContacto(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)    
    nombre = db.Column(db.String(64), nullable=False, unique=True)

class ContactoPersona(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)    
    persona_id = db.Column(db.Integer(), db.ForeignKey(Persona.id), nullable=False)
    tipocontacto_id = db.Column(db.Integer(), db.ForeignKey(TipoContacto.id), nullable=False)

class Usuario(UserMixin, Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    persona_id = db.Column(db.Integer(), db.ForeignKey(Persona.id), nullable=False)

class Posteo(Util, db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    texto = db.Column(db.String(140), nullable=False)
    fecha = db.Column(db.DateTime, index=True, default=datetime.utcnow, nullable=False)
    usuario_id = db.Column(db.Integer(), db.ForeignKey(Usuario.id), nullable=False)

@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

#def __repr__(o) -> str:
#    return f"{o.to_dict()}"
#
#def to_dict(o):
#    return {field.name:getattr(o, field.name) for field in o.__table__.c}
