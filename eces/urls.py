from django.urls import path

from . import views

urlpatterns=[

	path('', views.AcceuilView.as_view(), name='acceuil'),
	path('departement/', views.DepartementListView.as_view(), name='departement_list'),
	path('filieres/', views.FiliereListView.as_view(), name='filiere_list'),

]
