from contact.models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type your first name',
            }
        ),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type your last name',
            }
        ),
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type your phone',
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Type your e-mail',
            }
        ),
    )
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )
