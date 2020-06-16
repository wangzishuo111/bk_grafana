# -*- coding: utf-8 -*-
from __future__ import absolute_import

__all__ = ['celery_app', 'RUN_VER', 'APP_CODE', 'SECRET_KEY', 'BK_URL', 'BASE_DIR']

import os

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from blueapps.core.celery import celery_app

# app 基本信息

# SaaS运行版本，如非必要请勿修改
RUN_VER = 'open'
# SaaS应用ID
APP_CODE = 'bkgrafana'
# SaaS安全密钥，注意请勿泄露该密钥
SECRET_KEY = '11c01470-455d-4f79-8b84-19a9f5c9cfc7'
# 蓝鲸SaaS平台URL，例如 http://paas.bking.com
BK_URL = 'http://paas.growing.com' 

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(
    __file__)))
