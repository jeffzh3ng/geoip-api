#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : jeffzhang
# @Time    : 2019/1/30
# @File    : manage.py
# @Desc    : ""


from app import api_app
from flask_restful import Api
from app.apis.geoip_api import GeoAPI, SourceIP, ReqCount

api = Api(api_app)
api.add_resource(SourceIP, '/')
api.add_resource(GeoAPI, '/api/<ip>', '/api/<ip>/<language>')
api.add_resource(ReqCount, '/count')


if __name__ == '__main__':
    api_app.run('127.0.0.1', 50020)
