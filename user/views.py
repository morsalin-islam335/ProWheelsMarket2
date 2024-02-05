from django.shortcuts import render, redirect

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string # eta

from django.contrib import messages
from car.models import Car

def home(request):
    cars = Car.objects.all()
    categories = Category.objects.all() # eigulo search by  brand er jaonno use korbo

    return render(request, 'home.html',{"cars":cars, "categories":categories})



from .forms import SignUpAsOwner1 as OwnerForm1, SignUpFormAsOwner2 as OwnerForm2, SignUpFormAsBuyer1 as BuyerForm1, SignUpAsBuyer2 as BuyerForm2

from company.models import Category 
def signUpAsOwner(request): # owner ekta company er multiple product add korta parba
    if request.user.is_authenticated:
        return redirect("profile") # authenticated user sign-up korta parba na.
    else:
        if request.method == "POST":
            informationForm =OwnerForm1(request.POST)
            profilePicForm = OwnerForm2(request.POST, request.FILES)
            if informationForm.is_valid() and profilePicForm.is_valid() :
                user = informationForm.save() # first a informationForm ka save korbo than seta ja object diba ta profilePic form er user hisaba set kora dita hoiba
                profilePic = profilePicForm.save(commit = False)
                profilePic.user = user # etar user user form er user hisaba set hoiba
                profilePic.save()

                messages.success(request, 'Congratulations! Owner Account Create Successfully.')
                return redirect('login')
        else:
            form1 = OwnerForm1() 
            form2 = OwnerForm2() # 2ta form ei render korbo
            # print(form2) 
            # print(form1)
      
        return render(request, 'signUp.html', {"form1":form1, "form2":form2})
    

        
def signUpAsBuyer(request):# buyer product add korta parba na. buy korta parba.
    if request.user.is_authenticated:
        return redirect("profile") # authenticated user sign-up korta parba na.
    else:
        if request.method == "POST":
            informationForm = BuyerForm1(request.POST) # eta just User Model er form
            profilePicForm = BuyerForm2(request.POST, request.FILES) # eta just profile pic er form
            if informationForm.is_valid() and profilePicForm.is_valid() :
                user = informationForm.save() # first a informationForm ka save korbo than seta ja object diba ta profilePic form er user hisaba set kora dita hoiba
                profilePic = profilePicForm.save(commit = False)
                profilePic.user = user # etar user user form er user hisaba set hoiba
                profilePic.save()

                messages.success(request, 'Congratulations! Account Create Successfully.')
                mailSubject = 'Sign Up Conformation mail'
                message = render_to_string('sign_up_mail.html',{'first_name':informationForm.cleaned_data.get('first_name'),"last_name":informationForm.cleaned_data.get("last_name")}) # eta template ka string a convert korba
                to_email = informationForm.cleaned_data.get("email")
                # send_email = EmailMessage(mailSubject, message, to = [to_email]) # chaila multiple email a message send kora jaba
                send_email = EmailMultiAlternatives(mailSubject, '', to = [to_email]) # chaila multiple email a message send kora jaba
                send_email.attach_alternative(message, 'text/html') # mail a attach korbo and message ki typer hoba seta hoccha text/html
                
                send_email.send()

                return redirect('login')
            else:
                messages.warning(request, 'Your Form data is not valid.')
        
        form1 = BuyerForm1(); 
        form2 = BuyerForm2() # 2ta form ei render korbo
        return render(request, 'signUp.html', {"form1":form1, "form2":form2})
        


from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout




from django.contrib import messages

# def userLogin(request):
#     if request.user.is_authenticated:
#         return redirect("profile") # ek bar log in korla ar korar proiojon nai.
#     else:

#         if request.method == "POST":
#             form = AuthenticationForm(request = request, data = request.POST)

#             if form.is_valid():
#                 user_name = form.cleaned_data['username']
#                 user_password = form.cleaned_data['password']

#                 user = authenticate(username = user_name, password = user_password)

#                 if user is not None:
#                     login(request, user)
#                     messages.success(request, "Login Successfully!")
                    
#                     return redirect("profile")
#                 else:
                    
#                     messages.warning(request, "log in information is incorrect")

#         else:
#             form  = AuthenticationForm()
#         return render(request, 'login.html', {"form":form})

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
class UserLogin(LoginView):
    model = User
    template_name = 'login.html'
    

    def form_valid(self, form):
        messages.success(self.request, 'login successful')
   
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)


    def get_success_url(self) -> str:
        return  reverse_lazy('profile')
    
    

def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    buyingProduct = Car.objects.filter(buyer = request.user) # jodi kono product buy kora thaka tahola sei objectgulo return korba ar na hoila None return korba # kono owner o onno brand er product buy korta parba.

    try:# ei feature shudhu matro owner er jonno. owner tar add kora sob product tar profile a dekhta parba.  jodi kono product thaka tahola ta return korba noyto None return korba
        owner = owner =request.user.applicationUser # buyer er applicationUser nama kicu nai. tai exceptin hoiba
        productOnMarket =Car.objects.filter(owner = owner)
    except:
        productOnMarket = None

    return render(request, 'profile.html', {"products":buyingProduct, "haveProducts":productOnMarket}) # jodi kono product buy kora thaka ta context hisaba pathaba


from django.views.generic import DetailView

# class UserProfile(DetailView):
#     template_name = 'profile.html'
#     model = User
    
#     def get_context_data(self, **kwargs):
#         context  = super().get_context_data(**kwargs)
#         buyingProduct = Car.objects.filter(buyer = self.request.user) # jodi kono product buy kora thaka tahola sei objectgulo return korba ar na hoila None return korba # kono owner o onno brand er product buy korta parba.

#         productOnMarket = None # etaka temp hisaba rakhlam
#         try:# ei feature shudhu matro owner er jonno. owner tar add kora sob product tar profile a dekhta parba.  jodi kono product thaka tahola ta return korba noyto None return korba
#             owner = owner = self.request.user.applicationUser # buyer er applicationUser nama kicu nai. tai exceptin hoiba
#             productOnMarket =Car.objects.filter(owner = owner)
#         except:
#             productOnMarket = None
        
#         context['products'] = buyingProduct
#         context['haveProducts'] = productOnMarket

#         return context
    




    
    


def UserLogout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    messages.success(request, 'logout successfully')
    return redirect("homepage")


# class UserLogout(LogoutView):
    # def get_success_url(self):
    #     if self.user.is_authenticated:
    #         logout(self.request)
    #     return reverse_lazy("homepage")

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash 


def changePasswordWithOldPassword(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if  request.method == "POST":
        form = PasswordChangeForm(user = request.user, data = request.POST) # eta keyword parameter  hisaba nay

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user) # er vitor a just parametter dila kaj hoia jay
            messages.success(request, 'Password Update Successfully.')
            return redirect("homepage")
    else:
        form = PasswordChangeForm(user = request.user)
    return render(request,'passwdChange.html', {"form":form})


