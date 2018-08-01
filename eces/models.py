from django.db import models

class Departement(models.Model):
  choix_dep=(
     ('Gestion','Gestion'),
     ('Informatique','Informatique'),
     ('Langues', 'Langues'),
     ('Polytechnique','Polytechnique'),
     ('Qualité','Qualité'),
     ('Transport et Logistique', 'Transport et Logistique'),
     )
  
  departement=models.CharField(max_length=255, choices=choix_dep, unique=True ,help_text='veuillez selectionner un Departement')


  def __str__(self):
  	return self.departement

class Option(models.Model):
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
  option=models.CharField(max_length=255, choices=choix_op, unique=True, help_text='veuillez selectionner une Option')
  departement=models.ForeignKey(Departement, on_delete=models.CASCADE)


  def __str__(self):
    return self.option



class Document(models.Model):
  titre=models.CharField(max_length=100, unique=True, help_text='veuillez selectionner le titre du document')
  Image=models.FileField(upload_to="Reperttoire_Images")
  fichier=models.FileField(upload_to="Reperttoire_Documets")
  description=models.TextField(blank=True,null=True) 
  option=models.ForeignKey(Option, on_delete=models.CASCADE)
   

  def __str__(self):
    return self.titre.title()







# Create your models here.
