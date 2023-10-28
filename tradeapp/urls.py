from . import views
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', views.BookView.as_view()),
]
