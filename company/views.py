from django.shortcuts import render,redirect

# Create your views here.

from . forms import addBrandForm
from .models import Category
def addBrand(request):
    if request.method == 'POST':
        form = addBrandForm(request.POST)

        if form.is_valid():
            form2 = form.save(commit = False)
            form2.owner = request.user.applicationUser
            form2.slug = form.cleaned_data['brand'].lower()
            form2.save()

            return redirect("homepage")
    else:
        form = addBrandForm()
    return render(request, 'addBrand.html', {"form":form})

from company.models import Category
from car . models import Car
def searchByBrand(request, slugField):
    brand = Category.objects.get(slug = slugField)
    cars = Car.objects.filter(brand = brand)

    categories = Category.objects.all() # eigulo search by  brand er jaonno use korbo

    return render(request, 'home.html',{"cars":cars, "categories":categories, "isFiltered":True})

