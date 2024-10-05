from django.shortcuts import render


def class_func(request):
    return render(request, 'class_template.html')
