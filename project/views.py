import threading
from multiprocessing import current_process
import time

from django.db import transaction
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


from .tasks import async_task
from .models import Project, Test
from .serializers import ListProject, ListUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ListUser


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ListProject

    @action(detail=True, methods=['post'], url_name="updatedesc", url_path="updatedesc")
    def update_description(self, request, *args, **kwargs):
        project = self.get_object()

        async_task.delay(project.pk, request.data['description'])
        return Response(data="test")

    @action(detail=False, methods=["get"], url_path="test", url_name="test")
    def test(self, request):
        time.sleep(2)
        # return Response(data=f"pid {current_process().pid} | tid {threading.current_thread().name}")
        return Response(data="test")

    @action(detail=False, methods=["post"], url_path="test2", url_name="test2")
    def test2(self, request):
        time.sleep(2)
        try:
            with transaction.atomic():
                test = Test.objects.select_for_update().get(pk=1)
                test.count += 1
                test.save()
            return Response(data="test")
        except Exception:
            return Response(data=None, status=500)
