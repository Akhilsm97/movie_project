from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('add_movies/', views.add_movie, name="add_movie"),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]