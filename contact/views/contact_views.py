from django.shortcuts import render
from django.shortcuts import get_object_or_404

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")

    context = {
        "site_title": "Contatos - ",
        "contacts": contacts,
    }

    return render(
        request,
        "contact/index.html",
        context=context,
    )


def contact(request, contact_id):
    sigle_contact = get_object_or_404(
        Contact.objects,
        pk=contact_id,
        show=True,
    )
    site_title = f"{sigle_contact.first_name} {sigle_contact.last_name} - "
    
    context = {
        "site_title": site_title,
        "contact": sigle_contact,
    }

    return render(
        request=request,
        template_name="contact/contact.html",
        context=context,
    )
