from flask import Flask
from flask import redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from models.Interval import Interval
from models.Group import Group
from models.Schedule import Schedule
from models.Lecturer import Lecturer
from models.Subject import Subject

from Routes.Lecturers import lecturers
from Routes.Intervals import intervals


app=Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

app.register_blueprint(lecturers)
app.register_blueprint(intervals)

if __name__ == '__main__':
    app.run()