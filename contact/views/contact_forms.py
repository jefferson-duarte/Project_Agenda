from contact.models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()

            messages.success(
                request,
                'Contact created successfully.'
            )
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    form = ContactForm()

    context = {
        'form': form,

    }

    return render(
        request,
        'contact/create.html',
        context
    )


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True,
        owner=request.user,
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
            messages.success(
                request,
                'Contact updated successfully'
            )
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )

    form = ContactForm(instance=contact)

    context = {
        'form': form,
    }

    return render(
        request,
        'contact/create.html',
        context
    )


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True,
        owner=request.user,
    )

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        messages.success(
            request,
            'Contact deleted successfully'
        )
        return redirect('contact:index')

    context = {
        'contact': contact,
        'confirmation': confirmation,
    }

    return render(
        request,
        'contact/contact.html',
        context,
    )
