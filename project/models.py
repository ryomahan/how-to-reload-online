from django.db import models
from django.contrib.auth.models import User


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project")
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="user")

    def __str__(self):
        return self.user.username


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Test(models.Model):
    count = models.BigIntegerField(default=0)


