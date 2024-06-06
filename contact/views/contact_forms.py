from contact.models import Contact
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm
from django.urls import reverse


def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
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


def update(request, contact_id):
    contact = get_object_or_404(
        Contact.objects.filter(id=contact_id).filter(show=True)
    )

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {
            'form': form,
            'form_action': form_action
        }

        if form.is_valid():
            contact = form.save()
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
