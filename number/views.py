from django.shortcuts import render, redirect
from . models import Number
from django.core.paginator import Paginator
from django.contrib import messages
from . models import FormVerificador
import sys


# funcao verificadora do menor duodigito
def SmallDuodigit(number):
    for num in range(2, sys.maxsize**10):
        multiple = int(number) * num
        if Duodigit(multiple):
            return multiple


# funcao verificadora de duodigito
def Duodigit(digit):
    value = str(digit)
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

    # forma a mensagem do menor duodigito
    multiple = f'O menor duodigito múltiplo de {number} é {SmallDuodigit(number)}'
    messages.add_message(request, messages.SUCCESS, multiple)

    if form.is_valid():
        form.save()
        return redirect('index')


def history(request):
    # faz a ordenacao por data e a divisao de paginas
    numbers = Number.objects.order_by('-date_time')
    paginator = Paginator(numbers, 4)
    page = request.GET.get('p')
    numbers = paginator.get_page(page)
    return render(request, 'number/history.html', {
        'numbers': numbers
    })
