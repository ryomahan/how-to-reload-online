"""
测试接口：/project/{pk}/updatedesc/
代码位置：project.views.ProjectViewSet:update_description
测试内容：运行本脚本，并在运行过程中多次调用 kill -HUP 重启 gunicorn 启动的 django 服务
测试结果：10 * 10 * 5 success
得出结论：使用 kill -HUP 重启 Django 服务不会导致视图中有 Celery 操作（例如：celery_task_name.delay()）的请求出问题
"""

import multiprocessing
import requests
from faker import Faker
import threading
import os
import random

result = {}
fake = Faker()


def multi_processing():
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=multi_thread)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


def multi_thread():
    result[str(os.getpid())] = {}
    url = 'http://localhost:8000/project'

    def send_request():
        result[str(os.getpid())][str(threading.current_thread().name)] = 0
        data = {
            "description": fake.phone_number()
        }
        for i in range(5):
            resp = requests.post(f"{url}/{random.randint(1, 1000)}/updatedesc/", data=data)
            if resp.status_code == 200 and resp.text == '"test"':
                result[str(os.getpid())][str(threading.current_thread().name)] = result[str(os.getpid())][str(threading.current_thread().name)] + 1

    threads = []
    for i in range(10):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(result)


if __name__ == '__main__':
    multi_processing()
