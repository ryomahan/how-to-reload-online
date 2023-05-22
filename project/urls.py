from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, UserViewSet

router = DefaultRouter()

router.register(r'user', UserViewSet, basename='user')
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = router.urls
