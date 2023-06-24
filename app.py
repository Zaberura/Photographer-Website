from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)


# DATABASE

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    season = db.Column(db.String(20), nullable=True)
    year = db.Column(db.String(4), nullable=True)
    city = db.Column(db.String(64), nullable=True)
    country = db.Column(db.String(64), nullable=True)
    photos = db.relationship('Photos', backref='project', lazy=True)
    tags = db.relationship('Tags', backref='project', lazy=True)

    def __repr__(self):
        return '<project added, id: %r>' % self.name


class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    gallery_order = db.Column(db.Integer, nullable=True, default=255)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)

    def __repr__(self):
        return '<photo added, id: %r>' % self.id


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

    def __repr__(self):
        return '<project added, id: %r>' % self.name


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
        if not project_name == '':
            new_project = Projects.query.filter_by(name=project_name).first()
            if not new_project:
                new_project = Projects(name=project_name)

            try:
                db.session.add(new_project)
                db.session.commit()
            except:
                return 'Issue Occurred'

        url = request.form['url']
        if not url == '':
            # default gallery num assignment
            gallery_order = Photos.query.order_by(Photos.gallery_order.desc()).first().gallery_order
            gallery_order += 1

            new_photo = Photos(photo_url=url, project_id=Projects.query.filter_by(name=project_name).first().id,
                               gallery_order=gallery_order)

            try:
                db.session.add(new_photo)
                db.session.commit()
            except:
                return 'Issue'

        return redirect('/admin')


# RUN

if __name__ == '__main__':
    app.run(debug=True)
