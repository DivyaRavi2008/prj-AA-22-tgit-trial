from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/', views.TeamView.as_view()),
    url("",views.index, name = "index"),

]