from django.shortcuts import render
from .models import Serie
from .forms import SerieForm
# Create your views here.
def get_serie(request):
	qs=Serie.objects.all()
	form=SerieForm(request.POST or None)
	if request.method=='POST':
		if form .is_valid():
			form.save()
	form=SerieForm()
	context={
		'qs':qs
	}
	return render(request,'series.html',context)

	
