from flask import Blueprint, render_template, request

from pybo.models import Recycle
from pybo.models import Question
from .. import db

bp = Blueprint('recycle', __name__, url_prefix='/recycle')

@bp.route('/')
def _main():
    return render_template('recycle/recycle_main.html')

@bp.route('/list')
def _list():
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')

    # 조회
    recycle_list = Recycle.query.order_by(Recycle.item.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        recycle_list = recycle_list.filter(Recycle.item.like(search) | Recycle.division.like(search))

    recycle_list = recycle_list.paginate(page, per_page=10)
    return render_template('recycle/recycle_list.html', recycle_list=recycle_list, page=page, kw=kw)

@bp.route('/search')
def search():
    kw = request.args.get('kw', type=str, default='')
    # 조회
    recycle_list = Recycle.query.order_by(Recycle.item.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        recycle_list = recycle_list.filter(Recycle.division.like(search))
    return render_template('recycle/search.html', recycle_list=recycle_list, kw=kw)

@bp.route('/paper')
def paper():
    return render_template('recycle/paper.html')

@bp.route('/can')
def can():
    return render_template('recycle/can.html')

@bp.route('/glass')
def glass():
    return render_template('recycle/glass.html')

@bp.route('/plastic')
def plastic():
    return render_template('recycle/plastic.html')

@bp.route('/vinyl')
def vinyl():
    return render_template('recycle/vinyl.html')

@bp.route('/styrofoam')
def styrofoam():
    return render_template('recycle/styrofoam.html')
