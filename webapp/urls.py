from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, CrudPageView, ListPageView 
urlpatterns = [
    

    path('', HomePageView.as_view(), name = 'home'), 
    path('about/', AboutPageView.as_view(), name = 'about'), 
     path('contact/', ContactPageView.as_view(), name = 'contact'), 
      path('crud/', CrudPageView.as_view(), name = 'crud'), 
      path('list/', ListPageView.as_view(), name = 'list'), 
      
]
