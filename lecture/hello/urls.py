from django.urls import path

# . is mean from this folder
from . import views

urlpatterns =[
    # First argument is empty string which mean no additional argument
    # Second argemnue is what view should be rendered when this URL is visited
    path("", views.index, name="index"),
    path("atiwit", views.Atiwit, name="Atiwit"),
    path("cal", views.Cal, name="cal"),
    path("<str:name>", views.greet, name="greet")
]

