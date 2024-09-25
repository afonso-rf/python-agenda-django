from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Aqui veio do init"}),
        label="Primeiro nome",
        help_text="Texto para ajudar o usuario",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["first_name"].widget.attrs.update(
        #     {"placeholder": "Veio do init"}
        # )
        # self.fields["phone"].widget.attrs.update(
        #     {
        #         "pattern": "([0-9]{2}) [0-9]{4}-[0-9]{4}",
        #         "placeholder": "(XX) XXXX-XXXX",
        #     }
        # )

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "description",
            "category",
        )

        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "placeholder": "Primeiro nome",
        #         }
        #     ),
        # }

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
