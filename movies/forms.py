from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    open_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('contents',)