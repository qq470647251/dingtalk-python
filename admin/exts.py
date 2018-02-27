#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/2/27 下午1:58
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : exts.py
# @Software: PyCharm
from flask import Flask
from flask_script import Manager
from flask_migrate import MigrateCommand

__author__ = 'blackmatrix'


class CustomManager(Manager):

    def __call__(self, app=None, **kwargs):
        """
        自定义Manager为了去除Options will be ignored.的警告
        如果由flask-script的Manager创建app，和很多扩展结合使用都非常不方便。
        """
        if app is None:
            app = self.app
            if app is None:
                raise Exception("There is no app here. This is unlikely to work.")

        if isinstance(app, Flask):
            return app

        app = app(**kwargs)
        self.app = app
        return app

    def init_app(self, app):
        self.app = app
        # 增加db命令
        self.add_command('db', MigrateCommand)
        # 增加配置文件名的选项
        self.add_option('-e', '--env', dest='app_config', required=False)


# Flask-Script
manager = CustomManager()

if __name__ == '__main__':
    pass
