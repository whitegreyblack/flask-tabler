import yaml
from os import walk
from os.path import splitext
from types import SimpleNamespace as simpledict
from flask import Flask, jsonify, render_template

data_path = './data/'

app = Flask(__name__)
app.config['base'] = '.'

def parse_yaml_data(path, filename):
    with open(path + filename) as yaml_file:
        return yaml.load(yaml_file)

# config file
config_data = parse_yaml_data('./', 'config.yml')
app.config.update(config_data)

# data files
for _, _, files in walk(data_path):
    for f in files:
        filename = splitext(f)[0]
        file_data = parse_yaml_data(data_path, f)
        app.config[filename] = file_data

print(app.config['errors'])
# print(app.config['data'])

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

@app.route("/base")
def base():
    page = {
        'title': 'Page 404 Flask App',
        'body_class' : '',
        'rtl': False,
        'error': app.config['errors']['error-404'],
    }
    layout = {
        'title': "",
    }
    return render_template('error.html', site=app.config, page=page, content='Working?', layout=layout)

if __name__ == '__main__':
    app.run()