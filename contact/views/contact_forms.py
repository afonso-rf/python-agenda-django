from django.shortcuts import render, redirect

from contact.forms import ContactForm


def create(request):
    if request.method == "POST":
        forms = ContactForm(request.POST)
        context = {
            "site_title": "Create contact - ",
            "forms": forms,
        }

        if forms.is_valid():
            forms.save()
            return redirect("contact:create")

        return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )

    context = {
        "site_title": "Create Contact - ",
        "forms": ContactForm(),
    }

    return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )
