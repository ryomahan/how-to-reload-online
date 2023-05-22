
def init_project():
    from project.models import Project
    from faker import Faker
    fake = Faker()
    for i in range(1000):
        Project.objects.create(
            title=fake.name(),
            description=fake.text(),
            image=fake.image_url(),
            url=fake.url()
        )


def init_user():
    from django.contrib.auth.models import User
    from faker import Faker
    fake = Faker()
    for i in range(100):
        # create user info by fake
        username = fake.name()
        password = fake.password()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        # save username, password to user.json
        with open("user.json", "a") as f:
            f.write(f"{username}:{password}\n")


# a function delete user form id = 1 to id = 100
def delete_user():
    from django.contrib.auth.models import User
    for i in range(1, 101):
        User.objects.get(id=i).delete()


if __name__ == "__main__":
    # init django settings
    import os

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    import django

    django.setup()

    # init_project()
    # print("init project data success")
    # init_user()
    delete_user()
