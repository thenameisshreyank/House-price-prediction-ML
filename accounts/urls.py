from . import views
from django.urls import URLPattern, include, path

urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('adddata',views.adddata,name="adddata"),
    
   
]