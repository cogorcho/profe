import sqlite3
conn = sqlite3.connect('app.db')
sql = 'select name from pragma_table_info("{}") where pk=0'
tbs = "select name from sqlite_master where type = 'table' and name not like 'sqlite%' and name not like 'alembic%'"
cur = conn.cursor()
tablas = cur.execute(tbs).fetchall()
ltab = []

for tabla in tablas:
	ltab.append(tabla[0])
    


def gentoute(ruta, t, modelo, vari):
	print(f"@app.route('/{ruta}', methods=('GET','POST'))")
	print(f"@app.route('/{ruta}/<id>', methods=('GET','POST'))")
	print(f'def {ruta}(id=None):')
	print(f'\tform = {t.replace('_',' ').title().replace(' ','')}Form()')
	print(f'\tif form.validate_on_submit():')
	print('\t\tif id is not None:')
	print(f"\t\t\t{vari} = getById({modelo}, id)")
	print(f'\t\t\tif {vari} is None:')
	print(f'\t\t\t\terrmsg = "Datos erroneos para {modelo}"')
	print(f'\t\t\t\tflash(errmsg)')
	print(f"\t\t\t\treturn redirect(url_for('index'))")
	print('\t\t\telse:')
	colnames = cur.execute(sql.format(t))
	for colname in colnames:
		print(f"\t\t\t\t{vari}.{colname[0]} = form.{colname[0]}.data")
	print(f"\t\t\t\tdb.session.commit()")
	print(f"\t\t\t\treturn redirect(url_for('{vari}_tabla'))")
	print("\t\telse:")
	print(f"\t\t\t{vari} = {modelo}(")
	colnames = cur.execute(sql.format(t))
	for colname in colnames:
		print(f"\t\t\t\t\t{colname[0]} = form.{colname[0]}.data,")
	print(f"\t\t\t)")
	print(f"\t\t\tdb.session.add({vari})")
	print(f"\t\t\tdb.session.commit()")
	print(f"\t\t\treturn redirect(url_for('{vari}_tabla'))")

	print(f"\tif id is not None:")
	print(f"\t\t{vari} = getById({modelo}, id)")
	print(f'\t\tif {vari} is None:')
	print(f'\t\t\terrmsg = "Datos erroneos para {modelo}"')
	print(f'\t\t\tflash(errmsg)')
	print(f"\t\t\treturn redirect(url_for('index'))")

	colnames = cur.execute(sql.format(t))
	for colname in colnames:
		print(f"\t\tform.{colname[0]}.data = {vari}.{colname[0]}")

	print(f"\treturn render_template('{vari}.html', form=form)")


def gentab(modelo, vari, titulo):
	print(f"\n\n@app.route('/{vari}_tabla', methods=('GET',))")
	print(f"def {vari}_tabla():")
	print(f"\tcolnames = getColnames({modelo})")
	print(f"\trows = getRows({modelo})")
	print(f"\treturn render_template('tablas/{vari}.html', titulo='{titulo}', colnames=colnames, rows=rows)")


for t in ltab:
	colnames = cur.execute(sql.format(t))
	ruta = t.replace('_','').lower()
	modelo = t.replace('_',' ').title().replace(' ','')
	vari = t.replace('_','').lower()
	titulo = t.replace('_',' ').title()
	print("\n\n#'''")
	print(f"\tTable: {t}")
	print(f"\tORM Model: {modelo}")
	print(f"\tView: {vari}")
	print(f"\tRoute: @/{ruta}")
	print("'''")
	gentoute(ruta, t, modelo, vari)
	gentab(modelo, vari, titulo)
	
