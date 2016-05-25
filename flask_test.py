from flask import Flask

from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return b'<h1>home</h1>'

@app.route('/signin', methods=['get'])
def signin_form():
	return '''<form action="/signin" method="post">
				<p>username:<input name="username"></p>
				<p>password:<input type="password" name="passwd"></p>
				<p><button type="submit">Sign In</button></p>
				</form>'''

@app.route('/signin', methods=['post'])
def signin():
	if request.form["username"] == "admin" and request.form['passwd'] == "password":
		return '<h2>hello, admin!</h2>'
	return '<h2>Wrong Usernam or Wrong Password!</h2>'


if __name__ == '__main__':
	app.run()
	