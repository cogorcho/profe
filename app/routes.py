import json
from flask import render_template, flash, redirect, url_for, jsonify
from app import app, db
from app.forms import LoginForm ,RegistroForm ,AnioForm ,CargoDocenteForm ,CicloLectivoForm ,InstitucionForm ,MateriaForm ,PersonaForm ,TipoContactoForm ,TurnoForm ,ContactoPersonaForm ,DocenteForm ,UsuarioForm ,DocenteCargoForm ,PosteoForm ,AlumnoForm ,AlumnoComisionForm ,CarreraForm ,ComisionForm ,CuatrimestreForm ,MateriaDocenteForm ,MateriaPlanForm ,PlanEstudioForm
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Institucion,Carrera,CicloLectivo,Cuatrimestre,Turno,Materia,PlanEstudio,Anio,MateriaPlan,Persona,CargoDocente,Docente,DocenteCargo,MateriaDocente,Comision,Alumno,AlumnoComision,TipoContacto,ContactoPersona,Usuario,Posteo, vdocente

from datetime import datetime

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Juan Maria'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, title='Black Fart', posts=posts)


@app.route('/login', methods=('GET','POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(nombre=form.usuario.data).first()
        print(usuario)
        if usuario is None:
            flash('Nombre de usuario invalido')
            return redirect(url_for(ĺogin))
        login_user(usuario, remember=form.remember_me.data)
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Black Fart - Ingreso', form=form)

@app.route('/registro', methods=('GET','POST'))
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        p = Persona(
            apellido=form.apellido.data,
            nombre=form.nombre.data,
            dni=form.dni.data,
            fnacto=form.fnacto.data
        )
        db.session.add(p)
        db.session.flush()
        u = Usuario(
            nombre=form.usuario.data,
            persona_id=p.id,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(u)
        db.session.commit()
        flash(f'Requerimiento de ingreso para {form.apellido.data}, {form.nombre.data}')
        return redirect(url_for('index'))
    return render_template('registro.html', title='Black Fart - Registro', form=form)


'''
	Table: anio
	ORM Model: Anio
	View: anio
	Route: @/anio
'''
@app.route('/anio', methods=('GET','POST'))
@app.route('/anio/<id>', methods=('GET','POST'))
def anio(id=None):
	form = AnioForm()
	if form.validate_on_submit():
		if id is not None:
			anio = getById(Anio, id)
			if anio is None:
				errmsg = "Datos erroneos para Anio"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				anio.numero = form.numero.data
				db.session.commit()
				return redirect(url_for('anio_tabla'))
		else:
			anio = Anio(
					numero = form.numero.data,
			)
			db.session.add(anio)
			db.session.commit()
			return redirect(url_for('anio_tabla'))
	if id is not None:
		anio = getById(Anio, id)
		if anio is None:
			errmsg = "Datos erroneos para Anio"
			flash(errmsg)
			return redirect(url_for('index'))
		form.numero.data = anio.numero
	return render_template('anio.html', form=form)


@app.route('/anio_tabla', methods=('GET',))
def anio_tabla():
	colnames = getColnames(Anio)
	rows = getRows(Anio)
	return render_template('tablas/anio.html', titulo='Anio', colnames=colnames, rows=rows)


'''
	Table: cargo_docente
	ORM Model: CargoDocente
	View: cargodocente
	Route: @/cargodocente
'''
@app.route('/cargodocente', methods=('GET','POST'))
@app.route('/cargodocente/<id>', methods=('GET','POST'))
def cargodocente(id=None):
	form = CargoDocenteForm()
	if form.validate_on_submit():
		if id is not None:
			cargodocente = getById(CargoDocente, id)
			if cargodocente is None:
				errmsg = "Datos erroneos para CargoDocente"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				cargodocente.nombre = form.nombre.data
				db.session.commit()
				return redirect(url_for('cargodocente_tabla'))
		else:
			cargodocente = CargoDocente(
					nombre = form.nombre.data,
			)
			db.session.add(cargodocente)
			db.session.commit()
			return redirect(url_for('cargodocente_tabla'))
	if id is not None:
		cargodocente = getById(CargoDocente, id)
		if cargodocente is None:
			errmsg = "Datos erroneos para CargoDocente"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = cargodocente.nombre
	return render_template('cargodocente.html', form=form)


@app.route('/cargodocente_tabla', methods=('GET',))
def cargodocente_tabla():
	colnames = getColnames(CargoDocente)
	rows = getRows(CargoDocente)
	return render_template('tablas/cargodocente.html', titulo='Cargo Docente', colnames=colnames, rows=rows)


'''
	Table: ciclo_lectivo
	ORM Model: CicloLectivo
	View: ciclolectivo
	Route: @/ciclolectivo
'''
@app.route('/ciclolectivo', methods=('GET','POST'))
@app.route('/ciclolectivo/<id>', methods=('GET','POST'))
def ciclolectivo(id=None):
	form = CicloLectivoForm()
	if form.validate_on_submit():
		if id is not None:
			ciclolectivo = getById(CicloLectivo, id)
			if ciclolectivo is None:
				errmsg = "Datos erroneos para CicloLectivo"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				ciclolectivo.anio = form.anio.data
				ciclolectivo.finicio = form.finicio.data
				ciclolectivo.ffin = form.ffin.data
				db.session.commit()
				return redirect(url_for('ciclolectivo_tabla'))
		else:
			ciclolectivo = CicloLectivo(
					anio = form.anio.data,
					finicio = form.finicio.data,
					ffin = form.ffin.data,
			)
			db.session.add(ciclolectivo)
			db.session.commit()
			return redirect(url_for('ciclolectivo_tabla'))
	if id is not None:
		ciclolectivo = getById(CicloLectivo, id)
		if ciclolectivo is None:
			errmsg = "Datos erroneos para CicloLectivo"
			flash(errmsg)
			return redirect(url_for('index'))
		form.anio.data = ciclolectivo.anio
		form.finicio.data = ciclolectivo.finicio
		form.ffin.data = ciclolectivo.ffin
	return render_template('ciclolectivo.html', form=form)


@app.route('/ciclolectivo_tabla', methods=('GET',))
def ciclolectivo_tabla():
	colnames = getColnames(CicloLectivo)
	rows = getRows(CicloLectivo)
	return render_template('tablas/ciclolectivo.html', titulo='Ciclo Lectivo', colnames=colnames, rows=rows)


'''
	Table: institucion
	ORM Model: Institucion
	View: institucion
	Route: @/institucion
'''
@app.route('/institucion', methods=('GET','POST'))
@app.route('/institucion/<id>', methods=('GET','POST'))
def institucion(id=None):
	form = InstitucionForm()
	if form.validate_on_submit():
		if id is not None:
			institucion = getById(Institucion, id)
			if institucion is None:
				errmsg = "Datos erroneos para Institucion"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				institucion.nombre = form.nombre.data
				institucion.domicilio = form.domicilio.data
				db.session.commit()
				return redirect(url_for('institucion_tabla'))
		else:
			institucion = Institucion(
					nombre = form.nombre.data,
					domicilio = form.domicilio.data,
			)
			db.session.add(institucion)
			db.session.commit()
			return redirect(url_for('institucion_tabla'))
	if id is not None:
		institucion = getById(Institucion, id)
		if institucion is None:
			errmsg = "Datos erroneos para Institucion"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = institucion.nombre
		form.domicilio.data = institucion.domicilio
	return render_template('institucion.html', form=form)


@app.route('/institucion_tabla', methods=('GET',))
def institucion_tabla():
	colnames = getColnames(Institucion)
	rows = getRows(Institucion)
	return render_template('tablas/institucion.html', titulo='Institucion', colnames=colnames, rows=rows)


'''
	Table: materia
	ORM Model: Materia
	View: materia
	Route: @/materia
'''
@app.route('/materia', methods=('GET','POST'))
@app.route('/materia/<id>', methods=('GET','POST'))
def materia(id=None):
	form = MateriaForm()
	if form.validate_on_submit():
		if id is not None:
			materia = getById(Materia, id)
			if materia is None:
				errmsg = "Datos erroneos para Materia"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				materia.nombre = form.nombre.data
				db.session.commit()
				return redirect(url_for('materia_tabla'))
		else:
			materia = Materia(
					nombre = form.nombre.data,
			)
			db.session.add(materia)
			db.session.commit()
			return redirect(url_for('materia_tabla'))
	if id is not None:
		materia = getById(Materia, id)
		if materia is None:
			errmsg = "Datos erroneos para Materia"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = materia.nombre
	return render_template('materia.html', form=form)


@app.route('/materia_tabla', methods=('GET',))
def materia_tabla():
	colnames = getColnames(Materia)
	rows = getRows(Materia)
	return render_template('tablas/materia.html', titulo='Materia', colnames=colnames, rows=rows)


'''
	Table: persona
	ORM Model: Persona
	View: persona
	Route: @/persona
'''
@app.route('/persona', methods=('GET','POST'))
@app.route('/persona/<id>', methods=('GET','POST'))
def persona(id=None):
	form = PersonaForm()
	if form.validate_on_submit():
		if id is not None:
			persona = getById(Persona, id)
			if persona is None:
				errmsg = "Datos erroneos para Persona"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				persona.apellido = form.apellido.data
				persona.nombre = form.nombre.data
				persona.dni = form.dni.data
				persona.fnacto = form.fnacto.data
				db.session.commit()
				return redirect(url_for('persona_tabla'))
		else:
			persona = Persona(
					apellido = form.apellido.data,
					nombre = form.nombre.data,
					dni = form.dni.data,
					fnacto = form.fnacto.data,
			)
			db.session.add(persona)
			db.session.commit()
			return redirect(url_for('persona_tabla'))
	if id is not None:
		persona = getById(Persona, id)
		if persona is None:
			errmsg = "Datos erroneos para Persona"
			flash(errmsg)
			return redirect(url_for('index'))
		form.apellido.data = persona.apellido
		form.nombre.data = persona.nombre
		form.dni.data = persona.dni
		form.fnacto.data = persona.fnacto
	return render_template('persona.html', form=form)


@app.route('/persona_tabla', methods=('GET',))
def persona_tabla():
	colnames = getColnames(Persona)
	rows = getRows(Persona)
	return render_template('tablas/persona.html', titulo='Persona', colnames=colnames, rows=rows)


'''
	Table: tipo_contacto
	ORM Model: TipoContacto
	View: tipocontacto
	Route: @/tipocontacto
'''
@app.route('/tipocontacto', methods=('GET','POST'))
@app.route('/tipocontacto/<id>', methods=('GET','POST'))
def tipocontacto(id=None):
	form = TipoContactoForm()
	if form.validate_on_submit():
		if id is not None:
			tipocontacto = getById(TipoContacto, id)
			if tipocontacto is None:
				errmsg = "Datos erroneos para TipoContacto"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				tipocontacto.nombre = form.nombre.data
				db.session.commit()
				return redirect(url_for('tipocontacto_tabla'))
		else:
			tipocontacto = TipoContacto(
					nombre = form.nombre.data,
			)
			db.session.add(tipocontacto)
			db.session.commit()
			return redirect(url_for('tipocontacto_tabla'))
	if id is not None:
		tipocontacto = getById(TipoContacto, id)
		if tipocontacto is None:
			errmsg = "Datos erroneos para TipoContacto"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = tipocontacto.nombre
	return render_template('tipocontacto.html', form=form)


@app.route('/tipocontacto_tabla', methods=('GET',))
def tipocontacto_tabla():
	colnames = getColnames(TipoContacto)
	rows = getRows(TipoContacto)
	return render_template('tablas/tipocontacto.html', titulo='Tipo Contacto', colnames=colnames, rows=rows)


'''
	Table: turno
	ORM Model: Turno
	View: turno
	Route: @/turno
'''
@app.route('/turno', methods=('GET','POST'))
@app.route('/turno/<id>', methods=('GET','POST'))
def turno(id=None):
	form = TurnoForm()
	if form.validate_on_submit():
		if id is not None:
			turno = getById(Turno, id)
			if turno is None:
				errmsg = "Datos erroneos para Turno"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				turno.nombre = form.nombre.data
				db.session.commit()
				return redirect(url_for('turno_tabla'))
		else:
			turno = Turno(
					nombre = form.nombre.data,
			)
			db.session.add(turno)
			db.session.commit()
			return redirect(url_for('turno_tabla'))
	if id is not None:
		turno = getById(Turno, id)
		if turno is None:
			errmsg = "Datos erroneos para Turno"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = turno.nombre
	return render_template('turno.html', form=form)


@app.route('/turno_tabla', methods=('GET',))
def turno_tabla():
	colnames = getColnames(Turno)
	rows = getRows(Turno)
	return render_template('tablas/turno.html', titulo='Turno', colnames=colnames, rows=rows)


'''
	Table: contacto_persona
	ORM Model: ContactoPersona
	View: contactopersona
	Route: @/contactopersona
'''
@app.route('/contactopersona', methods=('GET','POST'))
@app.route('/contactopersona/<id>', methods=('GET','POST'))
def contactopersona(id=None):
	form = ContactoPersonaForm()
	if form.validate_on_submit():
		if id is not None:
			contactopersona = getById(ContactoPersona, id)
			if contactopersona is None:
				errmsg = "Datos erroneos para ContactoPersona"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				contactopersona.persona_id = form.persona_id.data
				contactopersona.tipocontacto_id = form.tipocontacto_id.data
				db.session.commit()
				return redirect(url_for('contactopersona_tabla'))
		else:
			contactopersona = ContactoPersona(
					persona_id = form.persona_id.data,
					tipocontacto_id = form.tipocontacto_id.data,
			)
			db.session.add(contactopersona)
			db.session.commit()
			return redirect(url_for('contactopersona_tabla'))
	if id is not None:
		contactopersona = getById(ContactoPersona, id)
		if contactopersona is None:
			errmsg = "Datos erroneos para ContactoPersona"
			flash(errmsg)
			return redirect(url_for('index'))
		form.persona_id.data = contactopersona.persona_id
		form.tipocontacto_id.data = contactopersona.tipocontacto_id
	return render_template('contactopersona.html', form=form)


@app.route('/contactopersona_tabla', methods=('GET',))
def contactopersona_tabla():
	colnames = getColnames(ContactoPersona)
	rows = getRows(ContactoPersona)
	return render_template('tablas/contactopersona.html', titulo='Contacto Persona', colnames=colnames, rows=rows)


'''
	Table: docente
	ORM Model: Docente
	View: docente
	Route: @/docente
'''
@app.route('/docente', methods=('GET','POST'))
@app.route('/docente/<id>', methods=('GET','POST'))
def docente(id=None):
	form = DocenteForm()
	if form.validate_on_submit():
		if id is not None:
			docente = getById(Docente, id)
			if docente is None:
				errmsg = "Datos erroneos para Docente"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				docente.legajo = form.legajo.data
				docente.persona_id = form.persona_id.data
				db.session.commit()
				return redirect(url_for('docente_tabla'))
		else:
			docente = Docente(
					legajo = form.legajo.data,
					persona_id = form.persona_id.data,
			)
			db.session.add(docente)
			db.session.commit()
			return redirect(url_for('docente_tabla'))
	if id is not None:
		docente = getById(Docente, id)
		if docente is None:
			errmsg = "Datos erroneos para Docente"
			flash(errmsg)
			return redirect(url_for('index'))
		form.legajo.data = docente.legajo
		form.persona_id.data = docente.persona_id
	return render_template('docente.html', form=form)


@app.route('/docente_tabla', methods=('GET',))
def docente_tabla():
	colnames = getColnames(vdocente)
	rows = getRows(vdocente)
	return render_template('tablas/docente.html', titulo='Docente', colnames=colnames, rows=rows)


'''
	Table: usuario
	ORM Model: Usuario
	View: usuario
	Route: @/usuario
'''
@app.route('/usuario', methods=('GET','POST'))
@app.route('/usuario/<id>', methods=('GET','POST'))
def usuario(id=None):
	form = UsuarioForm()
	if form.validate_on_submit():
		if id is not None:
			usuario = getById(Usuario, id)
			if usuario is None:
				errmsg = "Datos erroneos para Usuario"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				usuario.nombre = form.nombre.data
				usuario.password_hash = form.password_hash.data
				usuario.persona_id = form.persona_id.data
				db.session.commit()
				return redirect(url_for('usuario_tabla'))
		else:
			usuario = Usuario(
					nombre = form.nombre.data,
					password_hash = form.password_hash.data,
					persona_id = form.persona_id.data,
			)
			db.session.add(usuario)
			db.session.commit()
			return redirect(url_for('usuario_tabla'))
	if id is not None:
		usuario = getById(Usuario, id)
		if usuario is None:
			errmsg = "Datos erroneos para Usuario"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = usuario.nombre
		form.password_hash.data = usuario.password_hash
		form.persona_id.data = usuario.persona_id
	return render_template('usuario.html', form=form)


@app.route('/usuario_tabla', methods=('GET',))
def usuario_tabla():
	colnames = getColnames(Usuario)
	rows = getRows(Usuario)
	return render_template('tablas/usuario.html', titulo='Usuario', colnames=colnames, rows=rows)


'''
	Table: docente_cargo
	ORM Model: DocenteCargo
	View: docentecargo
	Route: @/docentecargo
'''
@app.route('/docentecargo', methods=('GET','POST'))
@app.route('/docentecargo/<id>', methods=('GET','POST'))
def docentecargo(id=None):
	form = DocenteCargoForm()
	if form.validate_on_submit():
		if id is not None:
			docentecargo = getById(DocenteCargo, id)
			if docentecargo is None:
				errmsg = "Datos erroneos para DocenteCargo"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				docentecargo.docente_id = form.docente_id.data
				docentecargo.cargodocente_id = form.cargodocente_id.data
				docentecargo.finicio = form.finicio.data
				docentecargo.ffin = form.ffin.data
				db.session.commit()
				return redirect(url_for('docentecargo_tabla'))
		else:
			docentecargo = DocenteCargo(
					docente_id = form.docente_id.data,
					cargodocente_id = form.cargodocente_id.data,
					finicio = form.finicio.data,
					ffin = form.ffin.data,
			)
			db.session.add(docentecargo)
			db.session.commit()
			return redirect(url_for('docentecargo_tabla'))
	if id is not None:
		docentecargo = getById(DocenteCargo, id)
		if docentecargo is None:
			errmsg = "Datos erroneos para DocenteCargo"
			flash(errmsg)
			return redirect(url_for('index'))
		form.docente_id.data = docentecargo.docente_id
		form.cargodocente_id.data = docentecargo.cargodocente_id
		form.finicio.data = docentecargo.finicio
		form.ffin.data = docentecargo.ffin
	return render_template('docentecargo.html', form=form)


@app.route('/docentecargo_tabla', methods=('GET',))
def docentecargo_tabla():
	colnames = getColnames(DocenteCargo)
	rows = getRows(DocenteCargo)
	return render_template('tablas/docentecargo.html', titulo='Docente Cargo', colnames=colnames, rows=rows)


'''
	Table: posteo
	ORM Model: Posteo
	View: posteo
	Route: @/posteo
'''
@app.route('/posteo', methods=('GET','POST'))
@app.route('/posteo/<id>', methods=('GET','POST'))
def posteo(id=None):
	form = PosteoForm()
	if form.validate_on_submit():
		if id is not None:
			posteo = getById(Posteo, id)
			if posteo is None:
				errmsg = "Datos erroneos para Posteo"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				posteo.texto = form.texto.data
				posteo.fecha = form.fecha.data
				posteo.usuario_id = form.usuario_id.data
				db.session.commit()
				return redirect(url_for('posteo_tabla'))
		else:
			posteo = Posteo(
					texto = form.texto.data,
					fecha = form.fecha.data,
					usuario_id = form.usuario_id.data,
			)
			db.session.add(posteo)
			db.session.commit()
			return redirect(url_for('posteo_tabla'))
	if id is not None:
		posteo = getById(Posteo, id)
		if posteo is None:
			errmsg = "Datos erroneos para Posteo"
			flash(errmsg)
			return redirect(url_for('index'))
		form.texto.data = posteo.texto
		form.fecha.data = posteo.fecha
		form.usuario_id.data = posteo.usuario_id
	return render_template('posteo.html', form=form)


@app.route('/posteo_tabla', methods=('GET',))
def posteo_tabla():
	colnames = getColnames(Posteo)
	rows = getRows(Posteo)
	return render_template('tablas/posteo.html', titulo='Posteo', colnames=colnames, rows=rows)


'''
	Table: alumno
	ORM Model: Alumno
	View: alumno
	Route: @/alumno
'''
@app.route('/alumno', methods=('GET','POST'))
@app.route('/alumno/<id>', methods=('GET','POST'))
def alumno(id=None):
	form = AlumnoForm()
	if form.validate_on_submit():
		if id is not None:
			alumno = getById(Alumno, id)
			if alumno is None:
				errmsg = "Datos erroneos para Alumno"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				alumno.legajo = form.legajo.data
				alumno.persona_id = form.persona_id.data
				alumno.fingreso = form.fingreso.data
				alumno.fegreso = form.fegreso.data
				db.session.commit()
				return redirect(url_for('alumno_tabla'))
		else:
			alumno = Alumno(
					legajo = form.legajo.data,
					persona_id = form.persona_id.data,
					fingreso = form.fingreso.data,
					fegreso = form.fegreso.data,
			)
			db.session.add(alumno)
			db.session.commit()
			return redirect(url_for('alumno_tabla'))
	if id is not None:
		alumno = getById(Alumno, id)
		if alumno is None:
			errmsg = "Datos erroneos para Alumno"
			flash(errmsg)
			return redirect(url_for('index'))
		form.legajo.data = alumno.legajo
		form.persona_id.data = alumno.persona_id
		form.fingreso.data = alumno.fingreso
		form.fegreso.data = alumno.fegreso
	return render_template('alumno.html', form=form)


@app.route('/alumno_tabla', methods=('GET',))
def alumno_tabla():
	colnames = getColnames(Alumno)
	rows = getRows(Alumno)
	return render_template('tablas/alumno.html', titulo='Alumno', colnames=colnames, rows=rows)


'''
	Table: alumno_comision
	ORM Model: AlumnoComision
	View: alumnocomision
	Route: @/alumnocomision
'''
@app.route('/alumnocomision', methods=('GET','POST'))
@app.route('/alumnocomision/<id>', methods=('GET','POST'))
def alumnocomision(id=None):
	form = AlumnoComisionForm()
	if form.validate_on_submit():
		if id is not None:
			alumnocomision = getById(AlumnoComision, id)
			if alumnocomision is None:
				errmsg = "Datos erroneos para AlumnoComision"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				alumnocomision.comision_id = form.comision_id.data
				alumnocomision.alumno_id = form.alumno_id.data
				db.session.commit()
				return redirect(url_for('alumnocomision_tabla'))
		else:
			alumnocomision = AlumnoComision(
					comision_id = form.comision_id.data,
					alumno_id = form.alumno_id.data,
			)
			db.session.add(alumnocomision)
			db.session.commit()
			return redirect(url_for('alumnocomision_tabla'))
	if id is not None:
		alumnocomision = getById(AlumnoComision, id)
		if alumnocomision is None:
			errmsg = "Datos erroneos para AlumnoComision"
			flash(errmsg)
			return redirect(url_for('index'))
		form.comision_id.data = alumnocomision.comision_id
		form.alumno_id.data = alumnocomision.alumno_id
	return render_template('alumnocomision.html', form=form)


@app.route('/alumnocomision_tabla', methods=('GET',))
def alumnocomision_tabla():
	colnames = getColnames(AlumnoComision)
	rows = getRows(AlumnoComision)
	return render_template('tablas/alumnocomision.html', titulo='Alumno Comision', colnames=colnames, rows=rows)


'''
	Table: carrera
	ORM Model: Carrera
	View: carrera
	Route: @/carrera
'''
@app.route('/carrera', methods=('GET','POST'))
@app.route('/carrera/<id>', methods=('GET','POST'))
def carrera(id=None):
	form = CarreraForm()
	if form.validate_on_submit():
		if id is not None:
			carrera = getById(Carrera, id)
			if carrera is None:
				errmsg = "Datos erroneos para Carrera"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				carrera.institucion_id = form.institucion_id.data
				carrera.nombre = form.nombre.data
				carrera.anios = form.anios.data
				db.session.commit()
				return redirect(url_for('carrera_tabla'))
		else:
			carrera = Carrera(
					institucion_id = form.institucion_id.data,
					nombre = form.nombre.data,
					anios = form.anios.data,
			)
			db.session.add(carrera)
			db.session.commit()
			return redirect(url_for('carrera_tabla'))
	if id is not None:
		carrera = getById(Carrera, id)
		if carrera is None:
			errmsg = "Datos erroneos para Carrera"
			flash(errmsg)
			return redirect(url_for('index'))
		form.institucion_id.data = carrera.institucion_id
		form.nombre.data = carrera.nombre
		form.anios.data = carrera.anios
	return render_template('carrera.html', form=form)


@app.route('/carrera_tabla', methods=('GET',))
def carrera_tabla():
	colnames = getColnames(Carrera)
	rows = getRows(Carrera)
	return render_template('tablas/carrera.html', titulo='Carrera', colnames=colnames, rows=rows)


'''
	Table: comision
	ORM Model: Comision
	View: comision
	Route: @/comision
'''
@app.route('/comision', methods=('GET','POST'))
@app.route('/comision/<id>', methods=('GET','POST'))
def comision(id=None):
	form = ComisionForm()
	if form.validate_on_submit():
		if id is not None:
			comision = getById(Comision, id)
			if comision is None:
				errmsg = "Datos erroneos para Comision"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				comision.ciclolectivo_id = form.ciclolectivo_id.data
				comision.cuatrimestre_id = form.cuatrimestre_id.data
				comision.turno_id = form.turno_id.data
				comision.materiadocente_id = form.materiadocente_id.data
				db.session.commit()
				return redirect(url_for('comision_tabla'))
		else:
			comision = Comision(
					ciclolectivo_id = form.ciclolectivo_id.data,
					cuatrimestre_id = form.cuatrimestre_id.data,
					turno_id = form.turno_id.data,
					materiadocente_id = form.materiadocente_id.data,
			)
			db.session.add(comision)
			db.session.commit()
			return redirect(url_for('comision_tabla'))
	if id is not None:
		comision = getById(Comision, id)
		if comision is None:
			errmsg = "Datos erroneos para Comision"
			flash(errmsg)
			return redirect(url_for('index'))
		form.ciclolectivo_id.data = comision.ciclolectivo_id
		form.cuatrimestre_id.data = comision.cuatrimestre_id
		form.turno_id.data = comision.turno_id
		form.materiadocente_id.data = comision.materiadocente_id
	return render_template('comision.html', form=form)


@app.route('/comision_tabla', methods=('GET',))
def comision_tabla():
	colnames = getColnames(Comision)
	rows = getRows(Comision)
	return render_template('tablas/comision.html', titulo='Comision', colnames=colnames, rows=rows)


'''
	Table: cuatrimestre
	ORM Model: Cuatrimestre
	View: cuatrimestre
	Route: @/cuatrimestre
'''
@app.route('/cuatrimestre', methods=('GET','POST'))
@app.route('/cuatrimestre/<id>', methods=('GET','POST'))
def cuatrimestre(id=None):
	form = CuatrimestreForm()
	if form.validate_on_submit():
		if id is not None:
			cuatrimestre = getById(Cuatrimestre, id)
			if cuatrimestre is None:
				errmsg = "Datos erroneos para Cuatrimestre"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				cuatrimestre.nombre = form.nombre.data
				cuatrimestre.ciclolectivo_id = form.ciclolectivo_id.data
				db.session.commit()
				return redirect(url_for('cuatrimestre_tabla'))
		else:
			cuatrimestre = Cuatrimestre(
					nombre = form.nombre.data,
					ciclolectivo_id = form.ciclolectivo_id.data,
			)
			db.session.add(cuatrimestre)
			db.session.commit()
			return redirect(url_for('cuatrimestre_tabla'))
	if id is not None:
		cuatrimestre = getById(Cuatrimestre, id)
		if cuatrimestre is None:
			errmsg = "Datos erroneos para Cuatrimestre"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = cuatrimestre.nombre
		form.ciclolectivo_id.data = cuatrimestre.ciclolectivo_id
	return render_template('cuatrimestre.html', form=form)


@app.route('/cuatrimestre_tabla', methods=('GET',))
def cuatrimestre_tabla():
	colnames = getColnames(Cuatrimestre)
	rows = getRows(Cuatrimestre)
	return render_template('tablas/cuatrimestre.html', titulo='Cuatrimestre', colnames=colnames, rows=rows)


'''
	Table: materia_docente
	ORM Model: MateriaDocente
	View: materiadocente
	Route: @/materiadocente
'''
@app.route('/materiadocente', methods=('GET','POST'))
@app.route('/materiadocente/<id>', methods=('GET','POST'))
def materiadocente(id=None):
	form = MateriaDocenteForm()
	if form.validate_on_submit():
		if id is not None:
			materiadocente = getById(MateriaDocente, id)
			if materiadocente is None:
				errmsg = "Datos erroneos para MateriaDocente"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				materiadocente.docente_id = form.docente_id.data
				materiadocente.materiaplan_id = form.materiaplan_id.data
				db.session.commit()
				return redirect(url_for('materiadocente_tabla'))
		else:
			materiadocente = MateriaDocente(
					docente_id = form.docente_id.data,
					materiaplan_id = form.materiaplan_id.data,
			)
			db.session.add(materiadocente)
			db.session.commit()
			return redirect(url_for('materiadocente_tabla'))
	if id is not None:
		materiadocente = getById(MateriaDocente, id)
		if materiadocente is None:
			errmsg = "Datos erroneos para MateriaDocente"
			flash(errmsg)
			return redirect(url_for('index'))
		form.docente_id.data = materiadocente.docente_id
		form.materiaplan_id.data = materiadocente.materiaplan_id
	return render_template('materiadocente.html', form=form)


@app.route('/materiadocente_tabla', methods=('GET',))
def materiadocente_tabla():
	colnames = getColnames(MateriaDocente)
	rows = getRows(MateriaDocente)
	return render_template('tablas/materiadocente.html', titulo='Materia Docente', colnames=colnames, rows=rows)


'''
	Table: materia_plan
	ORM Model: MateriaPlan
	View: materiaplan
	Route: @/materiaplan
'''
@app.route('/materiaplan', methods=('GET','POST'))
@app.route('/materiaplan/<id>', methods=('GET','POST'))
def materiaplan(id=None):
	form = MateriaPlanForm()
	if form.validate_on_submit():
		if id is not None:
			materiaplan = getById(MateriaPlan, id)
			if materiaplan is None:
				errmsg = "Datos erroneos para MateriaPlan"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				materiaplan.planestudio_id = form.planestudio_id.data
				materiaplan.materia_id = form.materia_id.data
				materiaplan.anio_id = form.anio_id.data
				db.session.commit()
				return redirect(url_for('materiaplan_tabla'))
		else:
			materiaplan = MateriaPlan(
					planestudio_id = form.planestudio_id.data,
					materia_id = form.materia_id.data,
					anio_id = form.anio_id.data,
			)
			db.session.add(materiaplan)
			db.session.commit()
			return redirect(url_for('materiaplan_tabla'))
	if id is not None:
		materiaplan = getById(MateriaPlan, id)
		if materiaplan is None:
			errmsg = "Datos erroneos para MateriaPlan"
			flash(errmsg)
			return redirect(url_for('index'))
		form.planestudio_id.data = materiaplan.planestudio_id
		form.materia_id.data = materiaplan.materia_id
		form.anio_id.data = materiaplan.anio_id
	return render_template('materiaplan.html', form=form)


@app.route('/materiaplan_tabla', methods=('GET',))
def materiaplan_tabla():
	colnames = getColnames(MateriaPlan)
	rows = getRows(MateriaPlan)
	return render_template('tablas/materiaplan.html', titulo='Materia Plan', colnames=colnames, rows=rows)


'''
	Table: plan_estudio
	ORM Model: PlanEstudio
	View: planestudio
	Route: @/planestudio
'''
@app.route('/planestudio', methods=('GET','POST'))
@app.route('/planestudio/<id>', methods=('GET','POST'))
def planestudio(id=None):
	form = PlanEstudioForm()
	if form.validate_on_submit():
		if id is not None:
			planestudio = getById(PlanEstudio, id)
			if planestudio is None:
				errmsg = "Datos erroneos para PlanEstudio"
				flash(errmsg)
				return redirect(url_for('index'))
			else:
				planestudio.nombre = form.nombre.data
				planestudio.finicio = form.finicio.data
				planestudio.ffin = form.ffin.data
				planestudio.carrera_id = form.carrera_id.data
				db.session.commit()
				return redirect(url_for('planestudio_tabla'))
		else:
			planestudio = PlanEstudio(
					nombre = form.nombre.data,
					finicio = form.finicio.data,
					ffin = form.ffin.data,
					carrera_id = form.carrera_id.data,
			)
			db.session.add(planestudio)
			db.session.commit()
			return redirect(url_for('planestudio_tabla'))
	if id is not None:
		planestudio = getById(PlanEstudio, id)
		if planestudio is None:
			errmsg = "Datos erroneos para PlanEstudio"
			flash(errmsg)
			return redirect(url_for('index'))
		form.nombre.data = planestudio.nombre
		form.finicio.data = planestudio.finicio
		form.ffin.data = planestudio.ffin
		form.carrera_id.data = planestudio.carrera_id
	return render_template('planestudio.html', form=form)


@app.route('/planestudio_tabla', methods=('GET',))
def planestudio_tabla():
	colnames = getColnames(PlanEstudio)
	rows = getRows(PlanEstudio)
	return render_template('tablas/planestudio.html', titulo='Plan Estudio', colnames=colnames, rows=rows)


def getRows(model,id=None):
    if id is None:
        print('getRows 1')
        #rows = db.session.execute(db.select(model)).fetchall()
        rows = model.query.all()
    else:
        print('getRows 2')
        #rows = db.session.execute(db.select(model).where(model.id==id))
        rows = model.query.filter_by(id=id).first()
    return rows
    #data = []

#    for row in rows:
#        r = row._mapping._to_tuple_instance()
#        data.append(r[0].to_dict())
#    return data

def getColnames(model):
	cols = []
	for col in model.__table__._columns:
		cols.append(col.name)
          
	return cols

def getById(model, id):
	return model.query.filter_by(id=id).first()

def getByDNI(model, dni):
	return model.query.filter_by(dni=dni).first()
