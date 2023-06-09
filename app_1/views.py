from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import MoviesForm
from .models import Movie

# Create your views here.
def index(request):
    det = Movie.objects.all()
    context = {'det':det}
    return render(request, 'index.html', context)
def add_movie(request):
    if request.method =='POST':
        name = request.POST.get('movie_name')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        print(img)
        add = Movie(movie_name=name, desc=desc, img=img)
        if add:
            add.save()
            messages.info(request, 'Movie Added Successsfully')
            return redirect(index)
        else:
            messages.info(request, 'Movie Not Added Successfully')
            return redirect(add_movie)
    return render(request, 'add_movie.html')

def update(request, id):
    up = Movie.objects.get(id = id)
    form= MoviesForm(request.POST or None, instance=up)
    if form.is_valid():
        form.save()
        print('Form Data saved')
        return redirect(index)
    else:
        print('Form Data Not Submitted')

    context = {'form':form, 'up':up}
    return render(request, 'update.html', context)

def delete(request, id):
    if request.method == 'POST':
        dell = Movie.objects.get(id = id)
        dell.delete()
        return redirect(index)
    return render(request, 'delete.html')
