from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def index_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('Имя')
        phone = request.POST.get('Телефон')
        message = request.POST.get('Сообщение')
        print(f'{name},{phone}: {message}')
    return render(request, 'catalog/index_contacts.html')

