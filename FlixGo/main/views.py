from django.http import HttpRequest , HttpResponse, Http404 
from django.core.paginator import Paginator, Page, PageNotAnInteger

from django.utils.html import mark_safe
from django.shortcuts import render
from django.views import generic

from .forms import *
from .models import *
from typing import *
import json


class AboutView(generic.ListView):
    template_name = 'about.html'


    @staticmethod
    def __extract_all_data():
        
        context = {

        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class ActorsFilterView(generic.ListView):
    template_name = 'actor.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class CatalogView(generic.ListView):
    template_name = 'catalog1.html'
    paginate_by = 12

    @staticmethod
    def __extract_all_data():
        
        context = {

        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class MovieDetailView(generic.DetailView):
    template_name = 'details1.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class SerialDetailView(generic.DetailView):
    template_name = 'details2.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class HelpCenterView(generic.ListView):
    template_name = 'faq.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class PrivacyPolicyView(generic.DetailView):
    template_name = 'privacy.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())


class HomeListView(generic.ListView):
    template_name = 'index2.html'

    @staticmethod
    def __extract_all_data():
        
        context = {

        }

        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, self.template_name, context = self.__extract_all_data())



# class ProfileView(generic.ListView) # TODO: Think about this f*ck*ng  sh*t :)







