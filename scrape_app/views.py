from django.shortcuts import render

# Create your views here.
from background_task import background
from django.contrib.auth.models import User
from django import db

@background(schedule=5)
def test_task():
    print('Hello World')
    db.connections.close_all()