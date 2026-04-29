# views.py
from django.shortcuts import render, redirect
from .models import UserName
from .forms import NameForm


def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Проверка поля на пустоту перед сохранением
            name = form.cleaned_data['name']
            if not name.strip():  # проверка на пустой ввод
                return render(request, 'index.html', {'form': form, 'error_message': 'Имя не должно быть пустым!'})

            user_name = UserName(name=name)
            user_name.save()
            return redirect('welcome')

    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})


def welcome(request):
    latest_user = UserName.objects.last()  # получаем последнего зарегистрированного пользователя
    context = {
        'latest_user': latest_user,
    }
    return render(request, 'welcome.html', context)