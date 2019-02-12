#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : jeffzhang
# @Time    : 2019/1/30
# @File    : __init__.py.py
# @Desc    : ""


import re
from flask import request
from flask_restful import Resource
from app.tasks.geoip import geoip

count = 0


class GeoAPI(Resource):
    @staticmethod
    def get(ip, language='en'):
        """
        GET /api/<ip>
        GET /api/<ip>/<language>
        :return:
        """
        try:
            global count
            compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.'
                                    '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
            if compile_ip.match(ip):
                data = geoip(ip, language)
                count += 1
                return data
            else:
                return {'status': 'failed', 'message': 'Invalid IP Address', 'data': {}}
        except Exception as e:
            print(e)
            return {'status': 'failed', 'message': "The request was invalid", 'data': {}}


class SourceIP(Resource):
    @staticmethod
    def get():
        """
        GET /
        :return:
        """
        try:
            ip = request.remote_addr
            compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.'
                                    '(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
            if compile_ip.match(ip):
                data = geoip(ip, language='en')
                return data
            else:
                return {'status': 'failed', 'message': 'Invalid IP Address', 'data': {}}
        except Exception as e:
            print(e)
            return {'status': 'failed', 'message': "The request was invalid", 'data': {}}


class ReqCount(Resource):
    @staticmethod
    def get():
        """
        GET /count
        :return:
        """
        global count
        return {"count": count}
