from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Initialize database
db = SQLAlchemy()


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


# Logics

def add_project(name, **kwargs):

    allowed_kwargs = ['season', 'year', 'city', 'country']

    if not name == '':
        project = Projects.query.filter_by(name=name).first()

        if not project:
            new_project = Projects(name=name)
            for key, value in kwargs.items():
                if key in allowed_kwargs:
                    setattr(project, key, value)

        try:
            db.session.add(new_project)
            db.session.commit()
        except:
            return 'Issue Occurred'


def add_photo(url, project_name=None, **kwargs):

    allowed_kwargs = ['season', 'year', 'city', 'country']

    if not url == '':

        photo = Photos.query.filter_by(photo_url=url).first()

        if not photo:
            # by default gallery_order assignment
            gallery_order = Photos.query.order_by(Photos.gallery_order.desc()).first().gallery_order
            gallery_order += 1

            if project_name is None:
                photo = Photos(photo_url=url, gallery_order=gallery_order)
            else:
                project_id = Projects.query.filter_by(name=project_name).first().id
                photo = Photos(photo_url=url, project_id=project_id, gallery_order=gallery_order)

            for key, value in kwargs.items():
                if key in allowed_kwargs:
                    setattr(photo, key, value)

            try:
                db.session.add(photo)
                db.session.commit()
            except:
                return 'Issue Occurred'

