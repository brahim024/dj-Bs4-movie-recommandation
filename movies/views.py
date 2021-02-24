from django.shortcuts import render
from .forms import MovieForm
from models import Movie
# Create your views here.

def home(request):
    form=MovieForm(request.POST or None)
    if request.method='POST':
        if form.is_vald():
            form.save()
    form=MovieForm()
    qs=Movie.objects.all()

    context={
        'form':form,
        'qs':qs
    }

    return render(request,'home.html',context)
