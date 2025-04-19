from app import app, db
from app.models import Institucion, Carrera, CicloLectivo, Cuatrimestre, Turno, PlanEstudios, Materia, Anio

institucion_id = None
carrera_id = None
ciclolectivo = None
cuatrimestres = None
materia_id = None
plan_id = None

def insert_institucion():
    i = Institucion(nombre='UTN Regional San Nicolas',domicilio='Colon 332, San Nicolas, Buenos Aires (2900)')
    db.session.add(i)
    db.session.commit()
    return i.id

def insert_carrera(institucion_id):
    c = Carrera(institucion_id=institucion_id, nombre='Tecnicatura Universitaria en Programacion', anios=2)
    db.session.add(c)
    db.session.commit()
    return c.id

def insert_ciclolectivo():
    cl = CicloLectivo(anio=2025)
    db.session.add(cl)
    db.session.commit()
    return cl.id

def insert_cuatrimestre(ciclolectivo_id):
    cua = Cuatrimestre(ciclolectivo_id=ciclolectivo_id, nombre='Primer')
    db.session.add(cua)
    cua = Cuatrimestre(ciclolectivo_id=ciclolectivo_id, nombre='Segundo')
    db.session.add(cua)
    db.session.commit()

def insert_turno():
    t = Turno(nombre='Mañana')
    db.session.add(t)
    t = Turno(nombre='Tarde')
    db.session.add(t)
    t = Turno(nombre='Noche')
    db.session.add(t)
    db.session.commit()

def insert_Materia():
    m = Materia(nombre='Bases de Datos II')
    db.session.add(m)
    m = Materia(nombre='Programación I')
    db.session.add(m)
    m = Materia(nombre='Arquitectura y Sistemas operativos')
    db.session.add(m)
    m = Materia(nombre='Matemática')
    db.session.add(m)
    m = Materia(nombre='Organización empresarial')
    db.session.add(m)
    m = Materia(nombre='Programación II')
    db.session.add(m)
    m = Materia(nombre='Probabilidad y Estadística 3')
    db.session.add(m)
    m = Materia(nombre='Base de Datos I')
    db.session.add(m)
    m = Materia(nombre='Inglés I')
    db.session.add(m)
    m = Materia(nombre='Programación III')
    db.session.add(m)
    m = Materia(nombre='Base de Datos II')
    db.session.add(m)
    m = Materia(nombre='Metodología de Sistemas I')
    db.session.add(m)
    m = Materia(nombre='Inglés II')
    db.session.add(m)
    m = Materia(nombre='Programación IV')
    db.session.add(m)
    m = Materia(nombre='Metodología de Sistemas II')
    db.session.add(m)
    m = Materia(nombre='Introducción al análisis de datos')
    db.session.add(m)
    m = Materia(nombre='Legislación')
    db.session.add(m)
    m = Materia(nombre='Gestión de desarrollo de software')
    db.session.add(m)
    db.session.commit()


def insert_PlanEstudio(carrera_id):
    pe = PlanEstudio(nombre='Plan TUP 2024', carrera_id=carrera_id)
    db.session.add(pe)
    db.session.commit()

def insert_Anio():
    a = Anio(numero=1)
    db.session.add(m)
    a = Anio(numero=2)
    db.session.add(m)
    db.session.commit()


def main():
    with app.app_context():
        #institucion_id = insert_institucion()
        #carrera_id = insert_carrera(institucion_id)
        #ciclolectivo_id = insert_ciclolectivo()
        #cuatrimestres = insert_cuatrinmestre(ciclolectivo_id)
        #insert_turno()
        #insert_Materia()
        #insert_PlanEstudio()

        #print(f'Institucion: {institucion_id}')
        #print(f'Carrera: {carrera_id}')
        #print(f'Ciclo  Lectivo: {ciclolectivo_id}')
        #for cua in cuatrimestres:
        #    print(f'Cuatrimestre: {cua}')

if __name__ == '__main__':
    main()

'''
https://testingbaires.com/tecnicas-de-control-de-concurrencia-en-base-de-datos/

https://www.datacamp.com/es/blog/sql-query-optimization

https://www.soydba.es/vistas-indexadas-de-sql-server/

https://certidevs.com/aprender-sql-seguridad-administracion

https://www.ibm.com/docs/es/imdm/11.6.0?topic=sswsr9-11-6-0-com-ibm-pim-adm-doc-data-admin-pim-con-dbmaintenance-html



https://learn.microsoft.com/es-es/sql/t-sql/language-elements/transactions-transact-sql?view=sql-server-ver16

https://dataiq.com.ar/blog/base-datos-aplicaciones-moviles/

insert into Materia_plan (planestudio_id, materia_id, anio_id)
select 1, id, 1
from Materia 
where nombre in (
'Programación I',
'Arquitectura y Sistemas operativos',
'Matemática',
'Organización empresarial',
'Programación II',
'Probabilidad y Estadística',
'Base de Datos I',
'Inglés I');

insert into Materia_plan (planestudio_id, materia_id, anio_id)
select 1, id, 2
from Materia 
where nombre in (
'Programación III',
'Base de Datos II',
'Metodología de Sistemas I',
'Inglés II',
'Programación IV',
'Metodología de Sistemas',
'Introducción al análisis de datos',
'Legislación',
'Gestión de desarrollo de software');

'''
