from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from .models import BookPost


class BookForm(forms.ModelForm):
    """
    https://django-crispy-forms.readthedocs.io/en/latest/layouts.html
    https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/
    """
    class Meta:
        model = BookPost
        fields = [
            'title',
            'book_author',
            'description',
            'genre',
            'condition',
            'reserved',
            'book_image',
            'owner_email',
            'owner_phone',
        ]
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('title'),
            Field('book_author'),
            Field('description', placeholder="Add the blurb here"),
            Field('genre'),
            Field('condition'),
            Field('reserved'),
            Field('book_image'),
            Field('owner_email'),
            Field('owner_phone'),
            Submit('submit', 'Add my Book!', css_class='btn btn-success'),
        )


