from django.urls import path 

from . views import addProduct, viewDetails, buyNow
urlpatterns = [
    path("addProduct/", addProduct, name = 'addProduct'),
    path("viewDetails/<int:id>/", viewDetails, name ='viewDetails'),
    path("buyNow/<int:id>", buyNow, name = "buyNow")
]
