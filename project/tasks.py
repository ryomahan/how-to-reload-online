from django.contrib.auth.models import User

from core.celery import app

from .models import Project


@app.task
def check_user_project_count():
    for user in User.objects.all():
        if user.project.count() > 100:
            print(f"User {user.username} has more than 100 projects")
        else:
            print(f"User {user.username} has less than 100 projects")


@app.task(name="async_task")
def async_task(project_id, desc):
    # 模拟阻塞 10 秒
    project = Project.objects.get(pk=project_id)
    import time
    time.sleep(1)
    project.description = desc
    project.save()
    print("async task done")
