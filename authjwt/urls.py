
from django.urls import path
from .views import cadaster_view, login_view, delete_view, edit_view

urlpatterns = [
    path("user/cadaster/", cadaster_view.as_view(), name="cadaster"),
    path("user/login/", login_view.as_view(), name="login"),
    path("user/edit/<str:username>/", edit_view.as_view(), name="edit"),
    path("user/delete/<str:username>/", delete_view.as_view(), name="delete"),
]