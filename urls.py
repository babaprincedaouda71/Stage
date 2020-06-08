from django.conf.urls import url
from pages import views
app_name = 'pages'
urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^allProduitsClient$', views.allProduitsClientView, name = 'allProduitsClient'),
    url(r'^allProduitsAdmin$', views.allProduitsAdminView, name = 'allProduitsAdmin'),
    url(r'^addProduit$', views.addProduitView, name = 'addProduit'),
    url(r'^updatePlusProduit/(?P<produit_id>\d+)/$', views.updatePlusProduitView, name = 'updatePlusProduit'),
    url(r'^updateMinusProduit/(?P<produit_id>\d+)/$', views.updateMinusProduitView, name = 'updateMinusProduit'),
    url(r'^base$', views.baseView, name = 'base'),
    url(r'^historique$', views.historiqueView, name = 'historique'),
]
