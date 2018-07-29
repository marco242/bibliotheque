from django.db import models

class Domaine(models.Model):
	libelle=models.CharField(max_length=255, unique=True, help_text="Ce champ nomme un domaie de manière unique")

	def __str__(self):
		return self.libelle.title()

# Create your models here.
