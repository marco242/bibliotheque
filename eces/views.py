from django.views.generic import TemplateView, ListView, DetailView

from . import models

class AcceuilView(TemplateView):
	template_name='base.html'

class DepartementListView(ListView):
	template_name='departement.html'
	model=models.Departement


class DepartementDetailView(DetailView):
	template_name='departement_detail.html'
	model=models.Departement

class FiliereListView(ListView):
	template_name='filieres.html'
	model=models.Filiere

class FiliereDetailView(DetailView):
	template_name='filieres_detail.html'
	model=models.Filiere

class DocumentListView(ListView):
	template_name='documents.html'
	model=models.Document

class DocumentDetailView(DetailView):
	template_name='documents_detail.html'
	model=models.Document





# Create your views here.
