# -*- coding: utf-8 -*-
# time: 2019/10/24 上午11:47
from tasks import app


@app.task
def sample():
    print("hello, world")
    return 100
