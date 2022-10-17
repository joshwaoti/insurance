from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Client, User

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class InsuranceForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('start_date',)

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'phone', 'password1', 'password2']

class Userform(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'phone', 'county']
