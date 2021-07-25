# from contacts.models import Contact
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # Get Form Values
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if the password match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'The username is taken')
                return redirect('register')
            else:

                # Look Good
                user = User.objects.create_user(
                    username=username,
                    password=password,
                )
                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in')
                # return redirect('index')
                user.save()
                messages.success(
                    request, 'You are now registered and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')