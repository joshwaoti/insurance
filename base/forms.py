from django.forms import ModelForm
from .models import Contact, Insuranced

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class InsuranceForm(ModelForm):
    class Meta:
        model = Insuranced
        fields = '__all__'
