from django.shortcuts import render

from contact.forms import ContactForm


def create(request):
    forms_ = ContactForm()

    if request.method == "POST":
        forms_ = ContactForm(request.POST)

    context = {
        "site_title": "Create Contact - ",
        "forms": forms_,
    }

    return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )
