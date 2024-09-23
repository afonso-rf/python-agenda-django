from django.urls import path

from contact import views

app_name = "contact"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("", views.index, name="index"),
    
    # Contact - CRUD
    path("contact/create/", views.create, name="create"),
    path("<int:contact_id>/", views.contact, name="contact"),
]
