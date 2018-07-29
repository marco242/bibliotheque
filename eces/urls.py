from django.urls import path
from . import views

urlpatterns=[

	path('', views.AcceuilView.as_view(), name='acceuil'),
	
]
