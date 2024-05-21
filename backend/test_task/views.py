from django.shortcuts import render
from django.core.exceptions import ValidationError
import requests
import validators

from .forms import RequestForm
from handlers.handlers import calling_a_request


# При попытке создать переменную со значениями сертификата и ключа поднималась
# ошибка. Поэтому до тех пор пока не решил бы проблему с подключением оставил
# значение сертификата и ключа в виде путей к файлам
CRT = 'test_task/certificate/client2024test.crt'

KEY = 'test_task/certificate/client2024test.key'


def index(request):
    """Вызов главной страницы с формой"""
    form = RequestForm()
    context = {'form': form}
    return render(request, 'test_task/get_input.html', context)


def get_response(request):
    """Страница со статусом ответа от вызванного сайта"""
    template = 'test_task/get_response.html'
    if request.POST:
        selected_method = request.POST['selected_method']
        url = request.POST['url']
        if not validators.url(url):
            raise ValidationError(
                'Ожидается url сайта'
            )
        result = calling_a_request(selected_method, url)
        data = {
            'selected_method': selected_method,
            'url': url,
            'result': result
        }
        print(data)
        return render(request, template, context=data)
    return render(request, template)


def get_test_task(request):
    """Вызов страницы указаной в ТЗ"""
    template = 'test_task/get_test_task.html'
    result = requests.get(
        'https://slb.medv.ru/api/v2/',
        cert=(CRT, KEY),
        verify=True
    )
    data = {
        'result': result.status_code
    }
    print(data)
    return render(request, template, context=data)
