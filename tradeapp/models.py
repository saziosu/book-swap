from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class BookPost(models.Model):
    """
    BookPost model for information on the user's book
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    post_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_posts'
    )
    book_author = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=30)
    # plan to change this to a form choice later
    condition = models.CharField(max_length=10)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reserved = models.BooleanField(default=False)
    book_image = CloudinaryField('book_image', default='placeholder')
    owner_email = models.EmailField()
    # will be updating this later for form
    owner_phone = models.TextField(max_length=10)

    class Meta:
        # order the posts on when they were created
        ordering = ['-created_on']

    def __str__(self):
        # django docs say to define this, returns a string from the class
        return self.title

    def save(self, *args, **kwargs):
        # method to automatically add slug from the title
        self.slug = slugify(self.title)
        super(BookPost, self).save(*args, **kwargs)
