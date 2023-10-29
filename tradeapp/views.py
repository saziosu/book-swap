from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BookPost


class BookView(generic.ListView):
    """
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    """
    model = BookPost
    queryset = BookPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'book_list'


class BookDetail(View):
    def get(self, request, slug, *arg, **kwarg):
        # only show published posts
        queryset = BookPost.objects.all()
        book = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "book_detail.html",
            {
                "book": book
            },
        )
