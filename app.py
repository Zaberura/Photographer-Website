from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)


# DATABASE

class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String(255), nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    gallery_order = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<photo added, id: %r>' % self.id


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    season = db.Column(db.String(20), nullable=True)
    year = db.Column(db.String(4), nullable=True)
    city = db.Column(db.String(64), nullable=True)
    country = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return '<project added, id: %r>' % self.name


# ROUTES

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return redirect('/')
    else:
        photos = Photos.query.order_by(Photos.gallery_order).all()
        urls = [photo.photo_url for photo in photos]
        #print(urls[0].photo_url)
        return render_template('gallery.html', urls=urls)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# RUN

if __name__ == '__main__':
    app.run(debug=True)