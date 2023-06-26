from flask import Flask, render_template, request, redirect, jsonify
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'

db.init_app(app)


# ROUTES

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('gallery.html', photos=get_all_photos())
    elif request.method == 'POST':
        return redirect('/')


@app.route('/projects')
def projects():
    all_projects = get_all_projects()
    return render_template('projects.html', projects=all_projects)


@app.route('/projects/<path:project_name>')
def project_name(project_name):

    return render_template('gallery.html', photos=get_project_photos(project_name))


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    elif request.method == 'POST':
        return ('Чудово', 200)


        # TODO sth with db
        # tmp = request.form
        # print("АХТУНГ АХТУНГ")
        # print(tmp)


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin.html')

    elif request.method == 'POST':

        project_name = request.form['project']
        add_project(project_name)

        photo_url = request.form['photo_url']
        add_photo(photo_url, project_name)

        return redirect('/admin')

# RUN

if __name__ == '__main__':
    app.run(debug=True)
