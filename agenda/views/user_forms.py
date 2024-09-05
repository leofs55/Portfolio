from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render, redirect
from agenda.forms import RegisterForm, RegisterUpdateForm


# def register(request):

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)

#         if form.is_valid():
#             form.save()

#     context = {
#         'form': RegisterForm()
#     }
#     return render(request, 'agenda/register.html', context)


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'O usuario foi salvo!')
            return redirect('agenda:index')

    context = {'form': form}

    return render(request, 'agenda/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso')
            return redirect('agenda:index')

        messages.error(request, 'Login invalido')
    context = {'form': form}

    return render(request, 'agenda/login.html', context)


@login_required(login_url='agenda:login')
def logout_view(request):
    auth.logout(request)
    return redirect('agenda:login')


@login_required(login_url='agenda:login')
def user_update(request):

    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            redirect('agenda:user_update')
        else:
            messages.error(request, 'Não foi possivel atulizar seus dados')

    context = {'form': form}
    return render(request, 'agenda/update_user.html', context)
