from django.http import HttpResponse


def index(request):
    return HttpResponse(content='Новое. У меня получилось!')


def second_page(request):
    return HttpResponse(content='А это вторая страница!')
