import random

from django.shortcuts import render, redirect


class Student:
    def __init__(self,name,age):
        self.age = age
        self.name = name


def index(request):
    context = {
        'title': 'Softuni Homepage',
        'value': random.random(),
        'students' : ['Pesho', 'Gosho', 'Mariano', 'Stamat'],
        'students2' : [],
        'values': list(range(20)),
        'stud': Student('Steve', 28)
    }

    return render(request, 'index.html', context)


def redirect_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')