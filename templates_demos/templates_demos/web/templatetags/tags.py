from Tools.scripts.ptags import tags
from django.template import Library

from templates_demos.web.views import Student

register = Library()

@register.simple_tag(name='student_info')
def show_student_info(student: Student):
    return f'Hi, I am {student.name} and I am {student.age} old'


@register.inclusion_tag('tags/nav.html', name='app_nav', takes_context=True)
def generate_nav(context,*args):
    context1 = {
        'url_names': args

    }

    return context1