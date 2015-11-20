# -*- coding=utf-8 -*-
from flask import Flask,render_template,request,make_response,redirect,abort
#from flask import request
#from flask import make_response
#from flask import redirect
#from flask import abort
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import Required,NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jiu shi yi ge random string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
	name = IntegerField('What is your name ?', validators=[Required(),NumberRange(min=-200,max=200,message='number overflow!')])
	submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template('index.html',current_time=datetime.utcnow(),form=form,name=name)

@app.route('/user/<name>')
def user(name):
	#user = load_user(id)
	if not user:
		abort(404)
	return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'),500

if __name__ == '__main__':
	manager.run()
	#app.run(host='192.168.1.51',port=80,debug=True)
