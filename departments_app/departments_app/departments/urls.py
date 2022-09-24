from django.urls import path

from departments_app.departments.views import home_page, \
    youtube  # show_departments, redirect_to_first_department, show_not_found,

urlpatterns = (
    path('', home_page),

    path('music/', youtube)

    # path('not-found/', show_not_found, name='not found'),

    # path('redirect/', redirect_to_first_department, name='first_department'),
    #
    # path('<department_id>/', show_departments, name='show department details'),
    #
    # path('int/<int:department_id>/', show_departments, name='show department')

)
