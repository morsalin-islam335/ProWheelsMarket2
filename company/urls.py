from django.urls import path 

from company import views

urlpatterns = [
    path("addBrand/", views.addBrand, name = 'addBrand'),
    path("searchByBrand/<slug:slugField>/", views.searchByBrand, name = 'searchByCategory')

    
]
