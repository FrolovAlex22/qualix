from django import forms


HTTP_METHODS = [
    ('get', 'Get'),
    ('post', 'Post')
]


class RequestForm(forms.Form):
    method = forms.ChoiceField(choices = HTTP_METHODS, label="Выберите метод")
    # forms.MultipleChoiceField(
    #     required=False,
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=HTTP_METHODS,
    # )
    url = forms.CharField(label="Пропишите URL")