from django.shortcuts import render
from django.views.generic import ListView
from .models import BookPost


class BookView(ListView):
    model = BookPost
    # queryset = BookPost.objects.all().order_by('-created_on'
    template_name = 'index.html'
