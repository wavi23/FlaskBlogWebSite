from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 't5d4D93si3m3tLMeyv1W171nOvQ3FO6Mt4g3jkQsm6mdlR2PWZL43WO1VvCGo2G2N8VG0nLPK72'

posts = [
	{
		'author': "Pedalinio",
		'title': "Tytuł posta 1",
		'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
		'date_posted': "22/02/2025"
	},
	{
		'author': "Pedalinio",
		'title': "Tytuł posta 2",
		'content': "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
		'date_posted': "23/02/2025"
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title="About")

@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title="Rejestracja", form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title="Logowanie", form=form)

if __name__ == '__main__':
	app.run(debug=True)