# -*- coding=utf-8 -*-
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	response = make_response('<h1>Hello World!</h1><br /><h1>Your browser is %s</h1><br /><h1>This document carries a cookie!</h1>' % user_agent)
	response.set_cookie('uid','001')
	#return redirect('http://www.baozhi360.com')
	return response
	#return '<h1>Hello World!</h1><br /><h1>Your browser is %s</h1>' % user_agent

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello,%s</h1>' % user.name

if __name__ == '__main__':
	manager.run()
	#app.run(host='192.168.1.51',port=80,debug=True)
