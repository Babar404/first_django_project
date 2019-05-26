from django.shortcuts import render
from django.views.generic import TemplateView    #built-in TemplateView to display our template

# Create your views here.
'''The TemplateView already contains all the logic
needed to display our template, we just need to specify the template’s name'''


class Home_page_view(TemplateView):
    template_name = 'home.html'    #is se ye faida hua k ab home page ka view home.html se uth kar ajaega

class About_page_view(TemplateView):
    template_name = 'about.html'









