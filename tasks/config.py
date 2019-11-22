# -*- coding: utf-8 -*-
# time: 2019/10/23 下午7:20
from kombu import Queue
from kombu import Exchange

result_serializer = "pickle"
broker_url = "redis://10.18.98.113"
result_backend = "mongodb://10.18.98.113:27017/celery"
timezone = "Asia/Shanghai"
imports = (
    "tasks.trainer",
)
include = ["tasks.trainer"]

# beat-schedule暂时用不上

task_queues = (
    Queue("default", exchange=Exchange("default"), routing_key="default"),
    Queue("trainer", exchange=Exchange("trainer"), routing_key="trainer.#")
)


task_routes = {
    'tasks.sample': {'queue': 'default'},
    "tasks.transfer_img": {"queue": "default"}
    }
