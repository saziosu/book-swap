from django.shortcuts import render
from django.views.generic import ListView
from .models import BookPost


class BookView(ListView):
    """
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    """
    model = BookPost
    queryset = BookPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'book_list'
