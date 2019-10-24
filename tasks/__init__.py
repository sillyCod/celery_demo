# -*- coding: utf-8 -*-
# time: 2019/10/24 上午11:34
from celery import Celery

app = Celery("demo")
app.config_from_object("tasks.config")
