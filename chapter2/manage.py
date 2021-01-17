#!/usr/bin/python3
# -*- coding:utf-8 -*-
from flask_script import Manager

from chapter2.flaskr import create_app

app = create_app()

manager = Manager(app)
if __name__ == '__main__':
    manager.run()
