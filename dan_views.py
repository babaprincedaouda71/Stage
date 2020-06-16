from django.shortcuts import render, redirect
from pages.models import Produit, Fournisseur, Depot, Historique, Statistic
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

def StatistiqueView(request):
    if request.method == 'POST':
        date1 = request.POST['dateDebut']
        date2 = request.POST['datefin']
        historique = Historique.objects.raw('WHERE date is between date1 and date2')
        return render(request,"pages/weeklyStat.html", {'historique': historique})
    else:
        historique = Statistic.objects.all()
    return render(request,"pages/statistics.html", {'historique': historique})



def weeklyStatistiqueView(request):
    if request.method == 'POST':
        dateDebut = request.POST['dateDebut']
        datefin = request.POST['datefin']
        historique = Historique.objects.raw('SELECT * FROM pages_historique   WHERE date between  %s and %s', [dateDebut,datefin])

        return render(request,"pages/weeklyStat.html", {'historique': historique})
    #historique= Historique.objects.raw('SELECT id,  qtePlus,date FROM pages_Produit  ')
    else:
        return render(request, "pages/weeklyStat.html",{'historique': historique})





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
            quantiteCommander = request.POST['quantiteCommander']
            quantiteRecue = request.POST['quantiteRecue']
            date_reception = request.POST['date_reception']
            photo = request.FILES['photo']
            produit = Produit(code_product = code_product, nom = nom, description = description, categorie = categorie, quantite = quantite, date_reception = date_reception, photo = photo)
            produit.save()
            historique = Historique(produit = produit, qteApres = quantite)
            historique.save()
            statistic = Statistic(produit = produit, stockRestant = quantite, stockCommande = quantiteCommander, stockRecue = quantiteRecue)
            statistic.save()
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
        statistic = Statistic.objects.get(produit = produit_id)
        statistic.stockRestant = quantites
        statistic.stockCommande = statistic.stockCommande + record.quantiteCommander
        statistic.stockRecue = statistic.stockRecue + qtePlus
        statistic.save()
        print(statistic.stockRestant)
        print(statistic.stockCommande)
        print(statistic.stockRecue)
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
        statistic = Statistic.objects.get(produit = produit_id)
        statistic.stockRestant = quantites
        statistic.stockCommande = statistic.stockCommande + record.quantiteCommander
        statistic.stockRecue = statistic.stockRecue + record.quantiteRecue
        statistic.stockRetirer = statistic.stockRetirer + qteMoins
        statistic.save()
        return redirect('pages:allProduitsAdmin')
    else:
        produits = Produit.objects.get(id = produit_id)
        return render(request, 'pages/updateMinusProduit.html', {'produits': produits})


def updateStaticsView(request, produit_id):
    if request.method == 'POST':
        nom = request.POST['nom']
        quantite = int(request.POST['quantite'])


        record = Produit.objects.get(id = produit_id)
        his = Historique.objects.get(id = produit_id)
        record.nom = nom
        record.save()
        qteRetirer = his.qteMoins
        qteRecue = record.quantiteRecue
        qteCom = record.quantiteCommander
        qteRest = record.quantite

        stat= Statistic(produit = record, stockRestant=qteRest, stockCommande=qteCom, stockRecue=qteRecue, stockRetirer=qteRetirer)

        stat.save()

        # history.produit.add(record)
        return redirect('pages:allProduitsAdmin')
    else:
        produits = Produit.objects.get(id = produit_id)
        return render(request, 'pages/allProduitsAdmin.html', {'produits': produits})
