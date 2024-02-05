from django.urls import path


# from django.contrib.auth.views import LogoutView
from user import views

urlpatterns = [
    path("", views.home, name = 'homepage'),
    path('signUpAsOwner/', views.signUpAsOwner, name = 'signUpAsOwner'),
    path('signUpAsBuyer/', views.signUpAsBuyer, name = 'signUpAsBuyer'),
    path('login/', views.UserLogin.as_view(), name = 'login'),
    # path("profile/", views.UserProfile.as_view(), name = 'profile'),
    path("profile/", views.profile, name = 'profile'),
    path('logOut/', views.UserLogout, name = 'logout'),
    # path("editInfo/", views.updateProfile, name = 'updateProfile'),
    path('changePassword/', views.changePasswordWithOldPassword, name = 'changePassword'),
    
]

