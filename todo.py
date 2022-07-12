from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from todoer.auth import login_required
from todoer.db import get_db


bp = Blueprint('todo', __name__)

@bp.route('/')
@login_required
def index():
    db, c = get_db()
    c.execute(
        'select t.id, t.description, u.username, t.completed, t.created_at from todo t JOIN user u on t.created_by = u.id order by created_at desc'
    )
    todos = c.fetchall()

    return render_template('todo/index.html', todos=todos)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    return render_template('todo/create.html')


@bp.route('/update', methods=['GET', 'POST'])
@login_required
def update():
    return ''
