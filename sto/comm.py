#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

import time
from autils import String
from hashlib import md5

TESTURL = "http://gateway-test.sto-express.cn:8088"


class Comm(object):

    def __get__(self, instance, type):
        self.appid = instance.appid
        self.secretkey = instance.secretkey
        self.sandbox = instance.sandbox
        return self

    def _get_request_header(self, content):
        timestamp = int(time.time())
        nonce = String.generate_strs(20)
        data = {
            "appid": self.appid,
            "timestamp": timestamp,
            "nonce": nonce,
            "sign": self._get_sign(content, timestamp, nonce)
        }
        return data

    def _get_sign(self, content, timestamp, nonce):
        """生成签名"""
        return md5(f'{content}{timestamp}{nonce}{self.secretkey}'.encode('utf-8')).hexdigest().lower()
