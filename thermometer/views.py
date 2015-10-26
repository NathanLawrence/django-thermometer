from django.shortcuts import render
from django.http import Http404

from thermometer.models import Therm

def index(request):
	therms = Therm.objects.all()
	return render(request, 'thermometer/index.html', {
		'therms': therms,
	})

def fetchsquare(request, id):
	try:
		therm = Therm.objects.get(id=id)
	except Therm.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'thermometer/fetchsquare.html', {
		'therm': therm,
	})