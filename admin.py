from django.contrib import admin
from pages.models import Produit, Fournisseur, Depot, Historique
# Register your models here.

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Depot)
admin.site.register(Historique)
