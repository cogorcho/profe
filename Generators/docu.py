from flask import Flask, render_template 

app = Flask(__name__) 
from flask_autodoc.autodoc import Autodoc 

auto = Autodoc(app) 

# GET API 
@app.route('/') 
def index(): 
	return render_template('index.html') 


# POST API 
@auto.doc() 
@app.route('/add', methods = ['POST']) 
def post_data(): 
	return render_template('form.html') 


# GET API with path param 
@app.route('/gfg/<int:page>') 
@auto.doc() 
def gfg(page): 
	return render_template('gfg.html', page=page) 

# This route generates HTML of documentation 
@app.route('/documentation') 
def documentation(): 
	return auto.html() 

if __name__ == '__main__': 
	app.run()

