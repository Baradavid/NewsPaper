from django import forms
from .models import Post

from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = [
            'title', 'text', 'author', 'categoryType', 'postCategory'
        ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        text = cleaned_data.get('text')

        if title == text:
            raise ValidationError(
                "Заголовок не должен быть идентичен тексту"
            )
        return cleaned_data

