from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Recycle

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo'

@bp.route('/')
def index():
    return redirect(url_for('recycle._main'))

@bp.route('/list')
def list():
    return redirect(url_for('recycle._list'))


@bp.route('/question')
def question():
    return redirect(url_for('question._list'))