from django.urls import path

from contact import views

app_name = "contact"

urlpatterns = [
    path(route="search/", view=views.search, name="search"),
    path(route="", view=views.index, name="index"),

    # Contact - CRUD
    path(route="contact/create/", view=views.create, name="create"),
    path(route="contact/<int:contact_id>/", view=views.contact, name="contact"),
    path(route="contact/<int:contact_id>/update/", view=views.update, name="update"),
    path(route="contact/<int:contact_id>/delete/", view=views.delete, name="delete"),

    # User
    path(route="user/create/", view=views.register, name="register"),
    path(route="user/login/", view=views.login_view, name="login"),
    path(route="user/logout/", view=views.logout_view, name="logout"),
    path(route="user/update/", view=views.user_update, name="user_update"),
]
