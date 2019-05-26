from django.urls import path  #standard hai
from .views import Home_page_view , About_page_view  # issi app me views ki file se meri class utha k laou

urlpatterns = [
    path('', Home_page_view.as_view(), name='home'),  #When using Class-Based Views, you always add as_view() at the end of the view name.
    path('about/', About_page_view.as_view(), name='about'),




]










