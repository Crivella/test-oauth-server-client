from django.urls import include, path

from . import views

# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'todo', views.IndexView, 'api_todo')
# router.register(r'user', views.UserView, 'api_user')

app_name = 'users'
urlpatterns = [
    path("", views.handshake, name="handshake"),
    path("download", views.download, name="download"),
]
