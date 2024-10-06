from django.shortcuts import render
from django.views.generic import TemplateView


def class_func(request):
    return render(request, 'second_task/class_template.html')


class func_temp(TemplateView):
    template_name = 'second_task/func_template.html'
