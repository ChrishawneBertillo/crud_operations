from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'app/home.html' 

class AboutPageView(TemplateView):
    template_name = 'app/about.html' 

class ContactPageView(TemplateView):
    template_name = 'app/contact.html' 

class CrudPageView(TemplateView): 
    template_name = 'app/crud.html' 


class ListPageView(TemplateView): 
    template_name = 'app/list.html' 


