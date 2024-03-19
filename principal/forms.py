from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)