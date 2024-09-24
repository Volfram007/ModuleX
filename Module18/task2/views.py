from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def class_template(request):
    return render(request, 'second_task/class_template.html')


def func_template(request):
    return render(request, 'second_task/func_template.html')
