from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

from .forms import RequestForm


def index(request):
    # Подключаем HTML-файл.
    template = loader.get_template('test_task/index.html')
    title = 'Страница запроса'
    context = {
        # Ключ словаря и имя переменной не обязательно называть одинаково,
        # но обычно это удобнее, чем использовать два разных имени.
        'title': title,
    }
    # Передаём в объект HttpResponse
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return HttpResponse(template.render({}, request))


def get_response(request):
    # Подключаем HTML-файл.
    form = RequestForm()
    template = loader.get_template('test_task/index.html')
    context = {'form': form}
    # Передаём в объект HttpResponse
    # HTML-код из загруженного файла, объект запроса request;
    # и возвращаем этот объект.
    return render(request, 'test_task/get.html', context)
