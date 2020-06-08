from django.shortcuts import render, redirect
from pages.models import Produit, Fournisseur, Depot, Historique
from pages.forms import addProduitForm

# Create your views here.

### Home
def home(request):
    return render(request, "pages/index1.html")



### base
def baseView(request):
    return render(request, "pages/base.html")



### Liste des produits Clients
def allProduitsClientView(request):
    produits = Produit.objects.all()
    return render(request, "pages/allProduitsClient.html", {'produits': produits})




### Liste des produits Admin
def allProduitsAdminView(request):
    produits = Produit.objects.all()
    return render(request, "pages/allProduitsAdmin.html", {'produits': produits})




### Historique des modifications
def historiqueView(request):
    history = Historique.objects.all()
    return render(request, "pages/historique.html", {'history': history})



### ajouter un produit
def addProduitView(request):
    if request.method == 'POST':
        form = addProduitForm(request.POST, request.FILES)
        if form.is_valid():
            code_product = request.POST['code_product']
            nom = request.POST['nom']
            description = request.POST['description']
            categorie = request.POST['categorie']
            quantite = request.POST['quantite']
            date_reception = request.POST['date_reception']
            photo = request.FILES['photo']
            produit = Produit(code_product = code_product, nom = nom, description = description, categorie = categorie, quantite = quantite, date_reception = date_reception, photo = photo)
            produit.save()
            return redirect('pages:allProduitsAdmin')
    else:
        form = addProduitForm()
        return render(request, "pages/addProduit.html", {'form': form})



### Mise a jour positive de la qte
def updatePlusProduitView(request, produit_id):
    if request.method == 'POST':
        nom = request.POST['nom']
        quantite = int(request.POST['quantite'])
        qtePlus = int(request.POST['qtePlus'])
        quantites = quantite+qtePlus
        record = Produit.objects.get(id = produit_id)
        print(record.code_product)
        print(record.nom)
        print(record.description)
        record.nom = nom
        record.quantite = quantites
        record.save()
        history = Historique(produit = record, qteAvant = quantite, qtePlus = qtePlus, qteApres = quantites)
        history.save()
        # history.produit.add(record)
        return redirect('pages:allProduitsAdmin')
    else:
        produits = Produit.objects.get(id = produit_id)
        return render(request, 'pages/updatePlusProduit.html', {'produits': produits})



### Mise a jour negative de la qte
def updateMinusProduitView(request, produit_id):
    if request.method == 'POST':
        nom = request.POST['nom']
        quantite = int(request.POST['quantite'])
        qteMoins = int(request.POST['qteMoins'])
        quantites = quantite-qteMoins
        record = Produit.objects.get(id = produit_id)
        print(record.code_product)
        print(record.nom)
        print(record.description)
        record.nom = nom
        record.quantite = quantites
        record.save()
        history = Historique(produit = record, qteAvant = quantite, qteMoins = qteMoins, qteApres = quantites)
        history.save()
        # history.produit.add(record)
        return redirect('pages:allProduitsAdmin')
    else:
        produits = Produit.objects.get(id = produit_id)
        return render(request, 'pages/updateMinusProduit.html', {'produits': produits})
