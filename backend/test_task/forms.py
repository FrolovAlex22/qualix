from django import forms


HTTP_METHODS = [
    ('GET', 'GET'),
    ('POST', 'POST')
]


class RequestForm(forms.Form):
    """Форма для ввода метода и данных вызываемого эндпойнта"""
    selected_method = forms.ChoiceField(
        choices=HTTP_METHODS,
        label='Выберите метод'
    )
    url = forms.CharField(
        help_text='Введите эндпоинт строкой, например: https://ya.ru',
        label='Пропишите URL'
    )
