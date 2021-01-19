from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from django.contrib.auth.models import Group 
from django.shortcuts import render
import os

register = template.Library()

# print(query)
class HomePage(TemplateView):
    template_name = 'index.html'
