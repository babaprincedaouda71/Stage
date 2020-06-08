from django import forms
from pages.models import Produit, Fournisseur, Depot

### Class django pour afficher le calendrier au niveau du formulaire
class dateInput(forms.DateInput):
####Le formulaire pour l'inscription du candidat####
    input_type = 'date'
class addProduitForm(forms.Form):
    code_product = forms.CharField(max_length = 10, label = "Code du produit")
    nom = forms.CharField(max_length = 50, label = "Nom")
    description = forms.CharField(max_length = 200, label = "Description")
    categorie = forms.CharField(max_length = 8, label = "Catégorie")
    quantite = forms.FloatField(label = "Quantité")
    date_reception = forms.DateField(label = "Date de reception", widget = dateInput)
    photo = forms.ImageField(label = "Photo")
    # fournisseur = forms.CharField(max_length = 8, label = "CIN")
    # depot = forms.CharField(max_length = 8, label = "CIN")
