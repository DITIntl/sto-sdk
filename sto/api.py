#!/usr/bin/python3
# @Time    : 2020-01-07
# @Author  : Kevin Kong (kfx2007@163.com)

from .comm import Comm

class STO(object):

    def __init__(self, appid, secretkey, sandbox=False):
        """
        初始化申通快递API
        param appid: appid
        param secretkey: secretkey
        sandbox: 是否沙箱环境
        """
        self.appid = appid
        self.secretkey = secretkey
        self.sandbox = sandbox

    comm = Comm()
