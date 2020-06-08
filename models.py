from django.db import models
from django.utils import timezone

# Create your models here.





class Fournisseur(models.Model):
    nom = models.CharField(max_length = 50, default="")
    telephone = models.CharField(max_length = 15, default = "")
    mail = models.CharField(max_length = 30, default = "")
    ville = models.CharField(max_length = 60, default = "")
    adresse = models.CharField(max_length = 60, default = "")
    type_reglement = models.CharField(max_length = 60, default = "")
    delai_paiement = models.CharField(max_length = 10, default = "")

    def __str__(self):
        return (self.nom)




class Depot(models.Model):
    nom = models.CharField(max_length = 50, default = "")
    ville = models.CharField(max_length = 50, default = "")
    adresse = models.CharField(max_length = 60, default = "")

    def __str__(self):
        return (self.nom)





class Produit(models.Model):
    code_product = models.CharField(max_length = 15, unique = True, null = False)
    nom = models.CharField(max_length = 50, default="")
    description = models.CharField(max_length = 200, default="")
    categorie = models.CharField(max_length = 50, default="")
    quantite = models.IntegerField()
    date_reception = models.DateField()
    photo = models.ImageField(default = "default.jpg", upload_to = 'produit_pics')
    # fournisseur = models.ManyToManyField(Fournisseur)
    # depot = models.ManyToManyField(Depot)

    def __str__(self):
        return (self.nom)




class Historique(models.Model):
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    qteAvant = models.IntegerField()
    qtePlus = models.IntegerField(null = True)
    qteMoins = models.IntegerField(null = True)
    qteApres = models.IntegerField()
    date = models.DateField(default = timezone.now)

    def __str__(self):
        return "%s %s %s" %(self.produit, self.qtePlus, self.date)
