
from . import views
from django.urls import path


urlpatterns=[
    path('',views.homepage,name="home"),
    
    path('product',views.product,name='product'),
    #path('answer',views.answer),
]