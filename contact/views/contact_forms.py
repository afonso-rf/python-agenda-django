from django.shortcuts import render

from contact.models import Contact

def create(request):
    if request.method == "POST":
        ...
    
    context = {
        "site_title": "Create Contact - ",
    }
    
    return render(
        request=request,
        template_name="contact/create.html",
        context=context,
    )