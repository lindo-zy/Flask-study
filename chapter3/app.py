#!/usr/bin/python3
# -*- coding:utf-8 -*-

from flask import Flask
from flask.views import View

app = Flask(__name__)


class ShowUers(View):
    methods = ['POST', 'GET']

    def dispatch_request(self):
        return '类视图'


class ListView(ShowUers):
    def get_template_name(self):
        return '没有这个模板'


app.add_url_rule('/users/', view_func=ListView.as_view('show_users'))

if __name__ == '__main__':
    app.run(debug=True)
