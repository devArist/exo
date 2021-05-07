from django.urls import path
from . import views 

app_name = 'siteweb'
urlpatterns = [
    path('', views.index , name = 'index'),
    path('about/', views.about , name = 'about'),
    path('contact/', views.contact , name = 'contact'),
    path('shop/', views.shop , name = 'shop'),
    path('shop_single', views.shop_single , name = 'shop_single'),
]