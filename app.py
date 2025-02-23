from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
	{
		'author': "Pedalinio",
		'title': "Tytuł posta 1",
		'content': "Opis posta 1",
		'date_posted': "22 Luty, 2025"
	},
	{
		'author': "Pedalinio",
		'title': "Tytył posta 2",
		'content': "Opis posta 2",
		'date_posted': "23 Luty, 2025"
	}
]

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html', title="About")

if __name__ == '__main__':
	app.run(debug=True)