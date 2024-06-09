from django.contrib import auth, messages
from django.shortcuts import render, redirect
from contact.forms import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'User created successfully.'
            )
            return redirect('contact:login')

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context
    )


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    if request.method != 'POST':
        return render(
            request,
            'contact/user_update.html',
            context,
        )

    form = RegisterUpdateForm(request.POST, instance=request.user)

    context = {
        'form': form
    }

    if not form.is_valid():
        messages.error(
            request,
            'Form is invalid.'
        )

        return render(
            request,
            'contact/user_update.html',
            context,
        )

    form.save()
    messages.success(
        request,
        'Register updated successfully.'
    )
    return redirect('contact:user_update')


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(
                request,
                'Logged in successfully.'
            )

            return redirect('contact:index')
        messages.error(
            request,
            'Login invalid.'
        )

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context
    )


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)

    messages.success(
        request,
        'Logged out successfully.'
    )
    return redirect('contact:login')
