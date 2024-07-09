from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg thick', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg thick', 'placeholder': 'E-mail'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 7, 'placeholder': 'Message'}))
