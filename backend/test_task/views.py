from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from .forms import RequestForm


def index(request):
    # Подключаем HTML-файл.
    form = RequestForm()
    template = loader.get_template('test_task/index.html')
    context = {'form': form}
    # Передаём в объект HttpResponse
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return render(request, 'test_task/get_input.html', context)


def get_response(request):
    form = RequestForm()
    template = loader.get_template('test_task/index.html')
    context = {'form': form}
    # Передаём в объект HttpResponse
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return render(request, 'test_task/get_input.html', context)
