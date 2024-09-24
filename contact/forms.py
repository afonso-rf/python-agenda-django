from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Aqui veio do init"
            }
        ),
        label="Primeiro nome",
        help_text="Texto para ajudar o usuario",
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # self.fields["first_name"].widget.attrs.update(
        #     {"placeholder": "Veio do init"}
        # )
        
        
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
        )

        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "placeholder": "Primeiro nome",
        #         }
        #     )
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data
        
        self.add_error(
            "first_name",
            ValidationError(
                message="Mensagem de erro",
                code="invalid",
            )
        )
        
        return super().clean()

    def clean_first_name(self):
        cleaned_data = self.cleaned_data.get("first_name")
        
        if cleaned_data == "ABC":
            raise ValidationError(
                "Não digite 'ABC' nesse campo",
                code="invalid",
            )
        
        return cleaned_data