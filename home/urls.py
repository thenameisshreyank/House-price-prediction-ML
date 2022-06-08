
from . import views
from django.urls import path


urlpatterns=[
    path('',views.homepage,name="home"),
    # path('register',views.register),
    # path('login',views.login),
    # path('signup',views.signup),
    # path('login',views.hlogin),
    # path('logout',views.hlogout),
    path('product',views.product,name='product'),
    #path('answer',views.answer),
]