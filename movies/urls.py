from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),

    path('<int:id>/detail/', views.detail, name="detail"),

    path('<int:id>/update/', views.update, name="update"),
]
