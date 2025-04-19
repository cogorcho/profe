import sqlite3
conn = sqlite3.connect('app.db')
sql = 'select name from pragma_table_info("{}") where pk=0'
tbs = "select name from sqlite_master where type = 'table' and name not like 'sqlite%' and name not like 'alembic%'"
cur = conn.cursor()
tablas = cur.execute(tbs).fetchall()
ltab = []
for tabla in tablas:
    ltab.append(tabla[0])

for t in ltab:
	fname = './app/templates/tablas/' + t.replace('_','').lower() + '.html'
	f = open(fname, "w")
	f.write("{% extends 'base.html' %}\n\n")
	f.write("{% block content %}\n")
	f.write(f"<h1>{t.replace('_',' ').title()}</h1>\n")
	f.write("<hr>\n")

	f.write('<table style="border: 1px solid black;">\n')

	f.write("\t<tr>\n")
	f.write("\t{% for col in colnames %} \n")
	f.write(f"\t\t<th>{{{{ col.title() }}}}</th>\n")
	f.write("\t{% endfor %}\n")
	f.write("\t</tr>\n")

	f.write("\t{% for row in rows %}\n")
	f.write("\t\t<tr>\n")
	f.write("\t\t{% for col in colnames %}\n")
	f.write("\t\t\t<td>{{ row[col] }}</td>\n")
	f.write("\t\t{% endfor %}\n")
	f.write("\t\t</tr>\n")	
	f.write("\t{% endfor %}\n")


	f.write("</table>\n")
	f.write("{% endblock %}\n")
	f.close()


'''
for o in rows:
    for val in o[0].__dict__.keys():
            if val.startswith('_sa'):
                    continue
            print(val,o[0].__dict__[val])
    print('-----------------------------------------')
    
    
for row in rows:
    for col in ['id','nombre','finicio','ffin']:
            print(f"<td>{row[0].__dict__[col]}</td>")
'''