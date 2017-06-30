from flask import Flask, render_template

my_first_app = Flask(__name__)

@my_first_app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	my_first_app.run(debug=True)