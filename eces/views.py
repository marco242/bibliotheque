from django.views.generic import TemplateView, ListView

from . import models

class AcceuilView(TemplateView):
	template_name='base.html'

class DepartementListView(ListView):
	template_name='departement.html'
	model=models.Departement

class FiliereListView(ListView):
	template_name='filieres.html'
	model=models.Filiere



# Create your views here.
