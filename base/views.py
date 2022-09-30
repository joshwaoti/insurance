from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm, InsuranceForm

def home(request):
    return render(request, 'base/index.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('base:home')
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'base/contact.html',context)


def insurance(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            phone_imei = form.cleaned_data['phone_imei']
            email_subject = 'phone insurance request'
            email_message = first_name + ' ' + last_name + '\n' + email + '\n' + 'phone number: ' + phone_number + '\n' + 'imei number: ' + phone_imei

            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return redirect ('base:home')

    form = InsuranceForm()
    context = {
        'form': form,
    }
    return render(request, 'base/insurance.html', context)