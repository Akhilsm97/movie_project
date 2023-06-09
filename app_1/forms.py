from .models import Movie
from django import forms


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields=[
                "movie_name",
                "desc",
                "img"
                ]
