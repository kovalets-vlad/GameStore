from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GameViewSet, GenreViewSet, report_view

router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'genres', GenreViewSet)

urlpatterns = [
    path('', include(router.urls)),       
    path('report/', report_view, name='report'), 
]
