import sqlite3

conn = sqlite3.connect('../app.db')

sql = 'select cid,name,type,"notnull" as nonul,dflt_value from pragma_table_info("{}") where pk=0'
tbs = "select name from sqlite_master where type = 'table' and name not like 'sqlite%' and name not like 'alembic%'"

cur = conn.cursor()
tablas = cur.execute(tbs).fetchall()

ltab = []
for tabla in tablas:
    ltab.append(tabla[0])

cnames = ['cid','name','type','nonull','dflt_value','pk']

for t in ltab:
    print('\nclass ' + t.replace('_',' ').title().replace(' ','')+'Form(FlaskForm):')
    #print(sql.format(t))
    cols = cur.execute(sql.format(t))
    for col in cols:
        o = dict(zip(cnames,list(col)))
        if o['type'] == 'INTEGER':
            tipo = 'IntegerField'
        if o['type'].startswith('VARCHAR'):
            s = o['type']
            lenf = s[s.find("(")+1:s.find(")")]
            tipo = 'StringField'
        if o['nonull'] == 1:
            inull = 'validators=[DataRequired()]'
        tname = o['name'].title()
        if o['type'] == 'DATETIME':
            tipo = 'DateField'
        print(f"\t{o['name']} = {tipo}('{tname}', {inull})")

#apellido = StringField('Apellido', validators=[DataRequired()])
#apellido = StringField('Apellido', validators=[DataRequired()])

#print(ltab)
