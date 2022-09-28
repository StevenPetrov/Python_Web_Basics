from django.urls import path

from templates_demos.web.views import index, redirect_home, about

urlpatterns = (
    path('', index, name='index'),
    path('home/', redirect_home, name='redirect to home'),
    path('about/', about, name='about'),
)