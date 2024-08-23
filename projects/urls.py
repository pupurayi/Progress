from django.contrib import admin
from django.urls import path
from .admin import TestScriptAdmin

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls,),
    
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:project_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:project_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:project_id>/vote/", views.vote, name="vote"),
]