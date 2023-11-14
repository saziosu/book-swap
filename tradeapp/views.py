from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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


class BookCreateView(LoginRequiredMixin, CreateView):
    """
    CreateView to create a new book post, sets the
    post_owner to the currently logged in user using the form.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def form_valid(self, form):
        """
        Method to set the owner of the post as the currently
        logged in user.
        https://www.youtube.com/watch?v=-s7e_Fy6NRU
        """
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    UpdateView to allow the user to update their book post.
    Only the owner of the post can edit it.
    """
    model = BookPost
    template_name = 'book_form.html'
    form_class = BookForm

    def test_func(self):
        """
        Method to only allow the post_owner of the book post to update that post
        https://stackoverflow.com/questions/65402719/updateview-and-preventing-users-from-editing-other-users-content
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False

    def form_valid(self, form):
        """
        Method to set the user that edited to the post_owner (post author)
        """
        form.instance.post_owner = self.request.user
        return super().form_valid(form)


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    DeleteView to delete the book posts, only allowed by the owner of the post.
    https://www.geeksforgeeks.org/deleteview-class-based-views-django/
    """
    model = BookPost

    def test_func(self):
        """
        Method to only allow the post_owner of the book post to delete that post
        https://stackoverflow.com/questions/65402719/updateview-and-preventing-users-from-editing-other-users-content
        """
        book = self.get_object()
        if self.request.user == book.post_owner:
            return True
        return False
    
    success_url = "/"
    template_name = 'book_delete.html'












