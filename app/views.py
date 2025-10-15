from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Category, Product, Customer, Order

def index(request: HttpRequest):
    return HttpResponse("Assalomu Alaykum")
