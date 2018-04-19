from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = { 'username': 'Sam' }
    return render_template('index.html', title='App', user=user)

@app.route("/layout")
def layout():
    return render_template('layout.html', numbers=numbers())

@app.route("/404")
def error404():
    return render_template('404.html')

@app.route('/500')
def error500():
    return render_template('500.html')

@app.route("/header")
def header():
    return render_template('header.html')

@app.route("/numbers")
def numbers():
    return jsonify({'0': 4, '1': 5, '2': 6})

if __name__ == '__main__':
    app.run()
