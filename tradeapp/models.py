from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField


class BookPost(models.Model):
    """
    BookPost model for information on the user's book
    """

    COND_CHOICES = (
        ('as_new', 'As New'),
        ('fine', 'Fine'),
        ('v_good', 'Very Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
    )

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title', max_length=200, unique=True)
    post_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_posts'
    )
    book_author = models.CharField(max_length=50)
    description = models.TextField()
    genre = models.CharField(max_length=30)
    condition = models.CharField(max_length=10, choices=COND_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reserved = models.BooleanField(default=False)
    book_image = CloudinaryField('book_image', default='placeholder')
    owner_email = models.EmailField()
    owner_phone = PhoneNumberField(region="IE")

    class Meta:
        # order the posts on when they were created
        # newest posts first
        ordering = ['-created_on']

    def __str__(self):
        # django docs say to define this, returns a string from the class
        return self.title

    def get_absolute_url(self):
        """
        Get absolute url to redirect the user to the page
        for the book they just posted.
        https://www.youtube.com/watch?v=-s7e_Fy6NRU
        https://ngangasn.com/what-is-get_absolute_url-in-django/
        """
        return reverse('book_detail', args=[str(self.slug)])
