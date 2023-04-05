from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ["title", "cover", "description"]
