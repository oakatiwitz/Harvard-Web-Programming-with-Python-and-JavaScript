from django.urls import path

from . import views

#prevent the same name in urls file such as the name index has both in newyear and task
app_name = "task"
urlpatterns =[
    path("", views.index, name="index"),
    path("add", views.add, name="add")

]