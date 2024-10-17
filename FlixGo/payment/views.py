from django.http import HttpRequest , HttpResponse, Http404 
from django.shortcuts import render
from django.views import generic
from .forms import *
from .models import *
from typing import *
import json