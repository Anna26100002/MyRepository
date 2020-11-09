from flask.blueprints import Blueprint
from flask import render_template
from models.Interval import Interval

intervals = Blueprint('intervals', __name__, template_folder='templates', static_folder='static')


@intervals.route('/intervals')
def index():
    return render_template('Index.html', intervals = Interval.query.all())
