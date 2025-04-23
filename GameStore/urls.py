from django.urls import include, path
from django.contrib import admin
from rest_framework import routers

from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),  
    path('api/auth/', include('authentication.urls')),
]