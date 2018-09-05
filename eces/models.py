from django.db import models
from ckeditor.fields import RichTextField

class Departement(models.Model):
  image=models.FileField(upload_to="Repertoire_Images", default='images_defaut/depdefault1.jpeg')
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer un departement')
  description=RichTextField()

#/multimedia/Repertoire_Images/164484340.jpg
  class Meta:
    ordering =('libelle',)
    verbose_name_plural='DEPARTEMENTS'
      


  def __str__(self):
     return self.libelle.title()




class Filiere(models.Model):
  image=models.FileField(upload_to="Repertoire_Images", default='images_defaut/filieredefaut1.jpg')
  libelle=models.CharField(max_length=255, unique=True ,help_text='veuillez indiquer une filiere')
  description=RichTextField()
  departement=models.ForeignKey(Departement, on_delete=models.CASCADE)

  class Meta:
    ordering =('libelle',)
    verbose_name_plural='FILIERES'
      


  def __str__(self):
    return self.libelle.title()



class Document(models.Model):
  titre=models.CharField(max_length=100, unique=True, help_text='veuillez indiquer le titre du document')
  description=RichTextField()
  image=models.FileField(upload_to="Repertoire_Images", default='images_defaut/defaultdocument.jpeg')
  fichier=models.FileField(upload_to="Repertoire_Documents")
  filiere=models.ForeignKey(Filiere, on_delete=models.CASCADE)

  class Meta:
    verbose_name_plural='DOCUMENTS'
   

  def __str__(self):
    return self.titre.title()







# Create your models here.
