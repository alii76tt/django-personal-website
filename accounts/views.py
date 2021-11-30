from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:index')
            else:
                messages.info(request, 'Disabled account.')

        else:
            messages.warning(request, 'Check your username and password!')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('account:login')
