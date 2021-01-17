#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    return '注册成功'
