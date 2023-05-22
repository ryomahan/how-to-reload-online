from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.urls')),
    # add django rest framework's url
    path('', include('rest_framework.urls'))
]
