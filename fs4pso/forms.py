from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('subject', 'name', 'good_points', 'improving_points', 'another_points',)