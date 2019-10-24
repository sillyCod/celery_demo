# -*- coding: utf-8 -*-
# time: 2019/10/23 下午7:20
from kombu import Queue
from kombu import Exchange

result_serializer = "json"
broker_url = "redis://localhost"
result_backend = "mongodb://localhost/celery"
timezone = "Asia/Shanghai"
imports = (
    "tasks.trainer",
)

# beat-schedule暂时用不上

task_queues = (
    Queue("default", exchange=Exchange("default"), routing_key="default"),
    Queue("trainer", exchange=Exchange("trainer"), routing_key="trainer.#")
)
