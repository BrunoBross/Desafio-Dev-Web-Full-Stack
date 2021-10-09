from django.shortcuts import render, redirect
from . models import Number
from django.core.paginator import Paginator
from django.contrib import messages
from . models import FormVerificador


def Duodigito(number):
    value = str(number)
    repeated = []
    distinct = 0

    for num in value:
        if num not in repeated:
            distinct += 1
        repeated.append(num)

    if 2 >= distinct:
        return True
    else:
        return False


def index(request):
    if request.method != 'POST':
        form = FormVerificador()
        return render(request, 'number/index.html', {'form': form})

    form = FormVerificador(request.POST, request.FILES)
    number = request.POST.get('numbers')
    if int(number) <= 100:
        messages.add_message(request, messages.ERROR, 'Digite um número maior que 100!')
        return render(request, 'number/index.html', {'form': form})
    if Duodigito(number):
        messages.add_message(request, messages.SUCCESS, 'É duodigito!')
    else:
        messages.add_message(request, messages.ERROR, 'Não é duodigito!')

    form.save()
    return redirect('index')


def history(request):
    numbers = Number.objects.order_by('-date_time')
    paginator = Paginator(numbers, 4)
    page = request.GET.get('p')
    numbers = paginator.get_page(page)
    return render(request, 'number/history.html', {
        'numbers': numbers
    })
