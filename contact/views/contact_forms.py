from django.shortcuts import render, redirect, get_list_or_404
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


def create(request):
    form_action = reverse("contact:create")

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        context = {
            "site_title": "Create contact - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect("contact:update", contact_id=contact.pk)

        return render(
            request=request,
            template_name="contact/create.html",
            context=context,
        )

    context = {
        "site_title": "Create Contact - ",
        "form": ContactForm(),
        "form_action": form_action,
    }

    return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )


def update(request, contact_id):
    contact, *_ = get_list_or_404(Contact.objects, pk=contact_id, show=True)

    form_action = reverse("contact:update", args=(contact_id,))

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            "site_title": "Update contact - ",
            "form": form,
            "form_action": form_action,
        }

        if form.is_valid():
            contact = form.save()
            return redirect("contact:update", contact_id=contact.pk)

        return render(
            request=request,
            template_name="contact/create.html",
            context=context,
        )

    context = {
        "site_title": "Update Contact - ",
        "form": ContactForm(instance=contact),
        "form_action": form_action,
    }

    return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )


def delete(request, contact_id):
    contact, *_ = get_list_or_404(Contact, pk=contact_id, show=True)
    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")

    return render(
        request=request,
        template_name="contact/contact.html",
        context={
            "contact": contact,
            "confirmation": confirmation,
        },
    )
