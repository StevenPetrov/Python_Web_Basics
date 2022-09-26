import random

from django.shortcuts import render


def index(request):
    context = {
        'title': 'Softuni Homepage',
        'value': random.random()
    }

    return render(request, 'index.html', context)