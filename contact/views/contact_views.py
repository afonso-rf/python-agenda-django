from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "site_title": "Contatos - ",
        "page_obj": page_obj,
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


def search(request):
    name_search = request.GET.get("q", "").strip()
    contacts_search = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=name_search)
        | Q(last_name__icontains=name_search)
        | Q(phone__icontains=name_search)
        | Q(email__icontains=name_search),
    )
    if name_search == "":
        return redirect("contact:index")

    input_value = name_search

    paginator = Paginator(contacts_search, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "site_title": "Search - ",
        "page_obj": page_obj,
        "input_value": input_value,
    }

    return render(
        request,
        template_name="contact/index.html",
        context=context,
    )
