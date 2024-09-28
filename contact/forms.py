from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from contact import models


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*",
            }
        ),
    )

    class Meta:
        model = models.Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
            "picture",
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name == last_name:
            msg = ValidationError(
                message="Segundo nome não pode ser igual ao primeiro",
                code="invalid",
            )

            self.add_error(field="first_name", error=msg)
            self.add_error(field="last_name", error=msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name == "ABC":
            # raise ValidationError(  # Utilizando o `raise`, o codigo para retornado a Excecao.
            #     "Não digite 'ABC' nesse campo",
            #     code="invalid",
            # )
            self.add_error(
                field="first_name",
                error=ValidationError(
                    "Não digite 'ABC' nesse campo",
                    code="invalid",
                ),
            )

        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            self.add_error(
                field="email",
                error=ValidationError(
                    message="Este email já existe.",
                ),
            )

        return email
