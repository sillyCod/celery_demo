# -*- coding: utf-8 -*-
# time: 2019/10/24 上午11:47
from tasks import app
from pathlib import Path


@app.task
def sample():
    print("hello, world")
    return 100


@app.task
def transfer_img(img, name):
    home = Path.home()
    path = home.joinpath(name).as_posix()
    with open(path, "wb") as f:
        f.write(img)
    return True
