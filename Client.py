from flask import Flask, render_template, redirect, url_for

from Server import Server

app = Flask(__name__)
server = Server()

# Registration Route
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')


# Welcome Route
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/')
def main_screen():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)