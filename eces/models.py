from django.db import models


class Bibliotheque(models.Model):
	choix_dep=(
     ('Gestion','Gestion'),
     ('Informatique','Informatique'),
     ('Langues', 'Langues'),
     ('Polytechnique','Polytechnique'),
     ('Qualité','Qualité'),
     ('Transport et Logistique', 'Transport et Logistique'),
     )
	choix_op=(
     ('Banque Finance Assurance','Banque Finance Assurance'),
     ('Commerce International','Commerce International'),
     ('Comptabilité Gestion Entreprise', 'Comptabilité Gestion Entreprise'),
     ('Electricité Industrielle','Electricité Industrielle'),
     ('Informatique de Gestion','Informatique de Gestion'),
     ('Gestion des Ressources Humaines', 'Gestion des Ressources Humains'),
     ('Langues et Affaires','Langues et Affaires'),
     ('Maintenance Industrielle','Maintenance Industrielle'),
     ('Management,Qualité,Securité et Environnement', 'Management,Qualité,Securité et Environnement'),
     ('Secretariat de Direction Bilingue','Secretariat de Direction Bilingue'),
     ('Transport et Logistique','Transport et Logistique'),
     ('Télécommunications et Reseaux', 'Télécommunications et Reseaux'),
     )

	departement=models.CharField(max_length=255, choices=choix_dep, help_text='veuillez selectionner un Departement')
	option=models.CharField(primary_key=True,max_length=255, choices=choix_op, help_text='veuillez selectionner une Option')
	titre=models.CharField(max_length=100, help_text='veuillez selectionner le titre du document')
	auteur=models.CharField(max_length=90)
	image=models.FileField(upload_to="Reperttoire_Images")
	fichier=models.FileField(upload_to="Reperttoire_Documets")
	description=models.TextField(blank=True,null=True) 


	def __str__(self):
		return self.departement+"----"+self.option+"----"+self.titre.title()+"----"+self.auteur


   



# Create your models here.
