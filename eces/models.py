from django.db import models

class Departement(models.Model):
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer un departement')
  description=models.TextField()


  class Meta:
    ordering =('libelle',)
      


  def __str__(self):
     return self.libelle.title()

class Filiere(models.Model):
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer une filiere')
  description=models.TextField()
  departement=models.ForeignKey(Departement, on_delete=models.CASCADE)

  class Meta:
    ordering =('libelle',)
      


  def __str__(self):
    return self.libelle.title()



class Document(models.Model):
  titre=models.CharField(max_length=100, unique=True, help_text='veuillez indiquer le titre du document')
  Image=models.FileField(upload_to="Repertoire_Images")
  fichier=models.FileField(upload_to="Repertoire_Documents")
  filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)
   

  def __str__(self):
    return self.titre.title()







# Create your models here.
