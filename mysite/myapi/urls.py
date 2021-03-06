# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls import url
router = routers.DefaultRouter()
router.register(r'users', views.UserProfileViewSet)
router.register(r'heroes', views.HeroViewSet)
router.register(r'register', views.UserViewSet),
router.register(r'userid', views.UserIdViewSet, base_name="UserId"),
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
   
    path('api/', include('rest_framework.urls', namespace='rest_framework'))

]
