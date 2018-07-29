from django.db import models

class Domaine(models.Model):
	libelle=models.CharField(max_length=255, unique=True, help_text="Ce champ nomme un domaie de manière unique")
	description=models.TextField()

	def __str__(self):
		return self.libelle.title()

class Categorie(models.Model):
	libelle=models.CharField(max_length=255, unique=True, help_text="Ce champ nomme une categorie de manière unique")
	domaine=models.ForeignKey(Domaine, on_delete=models.CASCADE)
	description=models.TextField()

	def __str__(self):
		return self.libelle.title()

class Document(models.Model):
	libelle=models.CharField(max_length=255, unique=True, help_text="Ce champ nomme une categorie de manière unique")
	categorie=models.ForeignKey(Categorie, on_delete=models.CASCADE)
	description=models.TextField(blank=True, null=True)
	image=models.FileField(upload_to='Document')
	fichier=models.FileField(upload_to='Document')

	def __str__(self):
		return self.libelle.title()







# Create your models here.
