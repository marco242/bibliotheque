from django.contrib import admin
from django.contrib.auth.models import Group,User
from . models import Departement, Filiere, Document


class FiliereInline(admin.StackedInline):
	model=Filiere
	extra=3

class DocumentInline(admin.StackedInline):
	model=Document
	extra=3


class DepartementAdmin(admin.ModelAdmin):
  list_display=('libelle', 'image')
  list_filter=('libelle',)
  ordering=('libelle',)
  summernote_fields=('libelle',)
  inlines=[
      FiliereInline,
  ]


  def has_add_permission(self, request):
    return True

 


class FiliereAdmin(admin.ModelAdmin):
  list_display=('libelle', 'image', 'departement')
  list_filter=('libelle',)
  ordering=('libelle',)
  search_fields=('libelle',)
  inlines=[DocumentInline,]
  list_per_page=5
 



class DocumentAdmin(admin.ModelAdmin):
  list_display=('titre', 'image', 'filiere')
  list_filter=('titre',)
  ordering=('titre',)
  search_fields=('titre', 'fichier')
  list_per_page=5


	

admin.site.unregister(Group)
#admin.site.register(User)

admin.site.register(Departement, DepartementAdmin)
admin.site.register(Filiere, FiliereAdmin)
admin.site.register(Document, DocumentAdmin)




# Register your models here.

