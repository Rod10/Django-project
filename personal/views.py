from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def homepage(request):
    return render(request=request,
                  template_name='personal/home.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="personal/register.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request = request,
                  template_name="personal/register.html",
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Deconnexion avec succes')
    return redirect('main:homepage')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "vous etez bien connecter")
                return redirect('main:homepage')
            else:
                return messages.error(request, "le nom d'utilisateur ou le mot de passe sont incorrects")
        else:
            return messages.error(request, "le nom d'utilisateur ou le mot de passe sont incorrects")

    form = AuthenticationForm()
    return render(request,
                  "personal/login.html",
                  {'form': form})

