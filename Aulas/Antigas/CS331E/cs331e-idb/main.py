# main.py (v.1.0)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/book/<int:id>/')
def book(id):
	return render_template('book.html', id=id)

if __name__ == "__main__":
	app.run()