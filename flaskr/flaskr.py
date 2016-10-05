# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

import os
from flask import Flask, request, session, redirect, url_for, abort, \
     render_template, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


def create_app():
    """ create our little application :)"""
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)

from models import *

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        q = request.form['amount']
        db.session.add(ETFOrder(request.form['amount'], 100))
        db.session.commit()
        return redirect(url_for('index'))
    #cur = db.session.execute('select id, ext, amount, price from orders order by id desc')
    cur = db.session.execute('select id, ext, amount, price from orders order by id desc')
    orders = cur.fetchall()
    return render_template('index.html', orders = orders)