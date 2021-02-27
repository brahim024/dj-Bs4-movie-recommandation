from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import MovieForm
from .models import Movie
# Create your views here.

def home(request):
    form=MovieForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid:
            form.save()
        
    form=MovieForm()
    qs=Movie.objects.all()

    context={
        'form':form,
        'qs':qs
    }

    return render(request,'movies/home.html',context)

class Deletemovie(DeleteView):
    model=Movie
    template_name='movies/confirm.html'
    success_url=reverse_lazy('movies:home')
