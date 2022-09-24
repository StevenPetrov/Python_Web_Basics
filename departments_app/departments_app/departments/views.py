from random import choice

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
from django.shortcuts import redirect, render


# def show_departments(request: HttpResponse, *args, **kwargs):
#     context = {
#         'page_title': 'Departments',
#         'method': request.method,
#         'order_by': request.GET.get('order_by', 'name')
#     }
#
#     return render(request, 'departments/templates/home.html', context)

#
# def redirect_to_first_department(request):
#     possible_order_by = ['age', 'id']
#     order_by = choice(possible_order_by)
#     return redirect(f'departments/?order_by={order_by}')

#
# def show_not_found(request):
#     result = render(request, 'departments/../../templates/404.html')
#     return HttpResponse(result)


def home_page(request):
    result = render(request, 'home.html')
    return HttpResponse(result)


def youtube(request):
    result = render(request, 'youtube.html')
    return HttpResponse(result)