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
    fname = './app/templates/' + t.replace('_','').lower() + '.html'
    f = open(fname, "w")
    f.write("{% extends 'base.html' %}\n\n")
    f.write("{% block content %}\n")
    f.write(f"<h1>{t.replace('_',' ').title()}</h1>\n")
    f.write("<hr>\n")
    f.write('<form action="" method="post" novalidate>\n')
    f.write("    {{ form.hidden_tag() }}\n")
    colnames = cur.execute(sql.format(t))
    for colname in colnames:
        f.write('\t<p>\n')
        f.write(f'\t{{{{ form.{colname[0]}.label }}}}<br>\n')
        f.write(f'\t{{{{ form.{colname[0]}(size=32) }}}}\n')
        f.write(f'\t{{% for error in form.{colname[0]}.errors %}}\n')
        f.write(f'\t\t<span style="color: red;">[{{{{ error }}}}]</span>\n')
        f.write(f'\t{{% endfor %}}\n')
        f.write('\t</p>\n')
    f.write("\t<p>{{ form.submit() }}</p>\n")
    f.write("</form>\n")
    f.write("{% endblock %}\n")
    f.close()

