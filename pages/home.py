from core import ModuleManager

from flask import Blueprint, redirect

app = Blueprint('private', __name__)


@app.route('/private')
def home_list():
    return 'private'
