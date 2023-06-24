from flask import Flask, render_template, request, redirect
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'

db.init_app(app)


# ROUTES

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        photos = Photos.query.order_by(Photos.gallery_order).all()
        urls = [photo.photo_url for photo in photos]
        return render_template('gallery.html', urls=urls)
    elif request.method == 'POST':
        return redirect('/')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


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
