from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def index_contacts(request):
    return render(request, 'catalog/index_contacts.html')

