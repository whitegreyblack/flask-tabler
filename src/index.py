import yaml
from os import walk
from os.path import splitext
from flask import Flask, jsonify, render_template

data_path = './data/'

app = Flask(__name__)
app.config['base'] = '.'
app.config['data'] = dict()

def parse_yaml_data(path, filename):
    with open(path + filename) as yaml_file:
        base_filename = splitext(filename)[0]
        file_contents = yaml.load(yaml_file)
        return base_filename, file_contents

# config file
config_filename, config_data = parse_yaml_data('./', 'config.yml')
app.config['data'][config_filename] = config_data

# data files
for _, _, files in walk(data_path):
    for f in files:
        filename, data = parse_yaml_data(data_path, f)
        app.config['data'][filename] = data

@app.route("/")
@app.route("/index")
def index():
    user = { 'username': 'Sam' }
    return render_template('index.html', title='App', user=user)

@app.route("/layout")
def layout():
    return render_template('layout.html', numbers=numbers())

@app.route("/400")
def error_bad_request():
    return render_template('400.html')

@app.route("/401")
def error_authorization():
    return render_template('401.html')

@app.route("/403")
def error_forbidden():
    return render_template('403.html')
    
@app.route("/404")
def error_not_found():
    return render_template('404.html')

@app.route("/410")
def error_gone():
    return render_template('410.html')

@app.route('/500')
def error_internal_server():
    return render_template('500.html')

@app.route('/503')
def error_service_unavailable():
    return render_template('503.html')

@app.route("/demo") 
def header():
    return render_template('header.html')

@app.route("/numbers")
def numbers():
    return jsonify({'0': 4, '1': 5, '2': 6})

@app.route("/base")
def base():
    page = {
        'title': 'base',
        'body_class' : '',
    }
    return render_template('base.html', site=app.config, page=page, content='Working?')

if __name__ == '__main__':
    app.run()