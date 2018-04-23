import yaml
from os import walk
from os.path import splitext
from types import SimpleNamespace as simpledict
from flask import Flask, jsonify, render_template

data_path = './data/'

app = Flask(__name__)
app.config['base'] = '.'
app.config['description'] = 'a responsive, flat and full featured admin template'
app.config['layout'] = { 'title': 'tabler-flask' }
app.config['page'] = {
    'title': 'Homepage',
    'body_class' : '',
    'rtl': False,
    'error': None,
}

# for key in app.config:
#     print(key)

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

for e, v in app.config['errors'].items():
    print(e, v)
# print(app.config['errors'])
# print(app.config['data'])

@app.route("/")
@app.route("/index")
def index():
    user = { 'username': 'Sam' }
    return render_template('index.html', title='App', user=user)

@app.route("/layout")
def layout():
    return render_template('layout.html', numbers=[1,2,3])

@app.route("/400")
def error_bad_request():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 400'
    app.config['page']['error'] = app.config['errors']['error-400']
    return render_template('error.html', site=app.config)

@app.route("/401")
def error_authorization():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 401'
    app.config['page']['error'] = app.config['errors']['error-401']
    return render_template('error.html', site=app.config)

@app.route("/403")
def error_forbidden():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 403'
    app.config['page']['error'] = app.config['errors']['error-403']
    return render_template('error.html', site=app.config)
    
@app.route("/404")
def error_not_found():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 404'
    app.config['page']['error'] = app.config['errors']['error-404']
    return render_template('error.html', site=app.config)

@app.errorhandler(404)
def page_not_found(e):
    '''Page handler for unfound resources'''
    app.config['page']['title'] = 'Page 404'
    app.config['page']['error'] = app.config['errors']['error-404']
    return render_template('error.html', site=app.config), 404

@app.route("/410")
def error_gone():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 410'
    app.config['page']['error'] = app.config['errors']['error-410']
    return render_template('error.html', site=app.config)

@app.route('/500')
def error_internal_server():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 500'
    app.config['page']['error'] = app.config['errors']['error-500']
    return render_template('error.html', site=app.config)

@app.route('/503')
def error_service_unavailable():
    '''Specific error request page'''
    app.config['page']['title'] = 'Page 503'
    app.config['page']['error'] = app.config['errors']['error-503']
    return render_template('error.html', site=app.config)

@app.route("/demo") 
def header():
    return render_template('header.html')

if __name__ == '__main__':
    app.run()