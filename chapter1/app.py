#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask, url_for, escape, abort, redirect

app = Flask(__name__)


# @app.route('/')
# def index():
#     return '这个是主页'
#
#
# @app.route('/user/<string:username>')
# def user(username):
#     return f'您的名字为：{username}'

@app.route('/')
def index():
    return redirect(url_for('other'))


@app.route('/index')
def other():
    return '这个是跳转网页'


@app.route('/login')
def login():
    abort(401)


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


@app.errorhandler(404)
def page_not_found(error):
    return 'page not found', 404


if __name__ == '__main__':
    app.run(debug=True)
