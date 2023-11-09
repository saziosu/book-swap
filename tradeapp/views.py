from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import BookPost
from .forms import BookForm


class BookView(generic.ListView):
    """
    https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-display/
    View from generic for viewing the current book posts
    """
    model = BookPost
    queryset = BookPost.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'book_list'


class BookDetail(View):
    """
    View to display the details of the book post to the user
    """

    def get(self, request, slug, *arg, **kwarg):
        queryset = BookPost.objects.all()
        book = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "book_detail.html",
            {
                "book": book
            },
        )


class BookCreateView(CreateView):
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def form_valid(self, form):
        """
        method to set the owner of the post as the currently
        logged in user.
        """
        form.instance.post_owner = self.request.user
        return super().form_valid(form)



