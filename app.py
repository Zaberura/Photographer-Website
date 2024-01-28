from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
from models import *

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'


db.init_app(app)


# ROUTES


@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':
    #     return render_template('gallery.html', photos=get_all_photos())
    # elif request.method == 'POST':
    #     return redirect('/')

    if request.method == 'GET':
        photos = get_all_photos()
        photos_link = {"data": [photo.photo_url for photo in photos]}
        return jsonify(photos_link)


@app.route('/projects')
def projects():
    if request.method == 'GET':

        all_projects = get_all_projects()
        _projects = [project.to_dict() for project in all_projects]
        return jsonify({"data": _projects})

    # return render_template('projects.html', projects=all_projects)


@app.route('/projects/<path:_project_name>')
def project_name(_project_name):

    project_photos = [project.to_dict() for project in get_project_photos(_project_name)]
    return jsonify({'data': project_photos})

    # return render_template('gallery.html', photos=get_project_photos(project_name))


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    elif request.method == 'POST':

        info = request.form
        print(info['name_input'])
        print('ALAAAAARm')
        return render_template('contact.html')


@app.route('/admin', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        return render_template('admin/admin.html')

    elif request.method == 'POST':

        user_input = request.form
        add_project(user_input['project_name'], season=user_input['season'],
                    year=user_input['year'], city=user_input['city'])
        add_photo(user_input['photo_url'], user_input['project_name'])

        return redirect('/admin')


if __name__ == '__main__':
    app.run(debug=True)
