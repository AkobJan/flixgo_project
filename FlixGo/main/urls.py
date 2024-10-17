from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeListView.as_view() , name='home'),
    path('about/', AboutView.as_view() , name='about'),
    path('actor/', ActorsFilterView.as_view() , name='actor'), # TODO: uuid for actor, slug
    path('catalog/', CatalogView.as_view() , name='catalog'), 
    path('movie/', MovieDetailView.as_view() , name='movie-detail'), # TODO: add unique indeactor
    path('serial/', SerialDetailView.as_view() , name='serial-detail'), # TODO: add unique indeactor
    path('faq/', HelpCenterView.as_view() , name='help-center'),
    path('privacy-policy', PrivacyPolicyView.as_view() , name='privacy'),
]
