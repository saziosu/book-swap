from . import views
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path('', views.BookView.as_view()),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
]
