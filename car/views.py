from django.shortcuts import render, redirect

# Create your views here.

from django.contrib import messages
from . forms import addCar
def addProduct(request):
    if not request.user.is_authenticated:
        return redirect("login")
    elif not request.user.applicationUser.isOwner: # jodi owner type user na hoy tahola product add korta parba na.
        return redirect('profile')
    if request.method == 'POST':
        form = addCar(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit = False)
            car.owner = request.user.applicationUser
            car.save()
            return redirect("homepage")
    else:
        form  = addCar()
    return render(request, 'addProduct.html', {"form":form})


from car.models import Car
from car.models import Comment
from .forms import CommentsForm # ek sathi  car er details ar comment form 2 tai context data hisaba pathata hoiba
def viewDetails(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            commentForm = CommentsForm(request.POST)
            if commentForm.is_valid():
                comment = commentForm.save(commit = False)
                comment.name = f"{request.user.first_name} {request.user.last_name}" # user er name capture korbo
                comment.save()
                return redirect(viewDetails, id = id) # parameter soho redirect kora pass korta hoiba.
            else:
                messages.success(request, 'comment form is not valid')
                return redirect("viewDetails", id = id)
        else:
            return redirect("login") # unauthenticated user login kora chara comment korta parba na
    else:
        commentForm = CommentsForm()
           
    car = Car.objects.get(id = id) 
    comments = Comment.objects.all() # sob gulo objects dhorlam 
    return render(request, 'viewDetails.html', {"car":car, 'form':commentForm, 'comments':comments})




def buyNow(request, id):
    # if request.method == "POST":  kono rokom condition check korar lagba na
    if not request.user.is_authenticated:
        return redirect("login") # unauthenticated user chaila buy korta parba na.
    car = Car.objects.get(id = id)
    car.quantity -= 1
    car.buyer = request.user # buyer kanar satha satha tar record a add hoiba
    car.save()
    return redirect("profile")
