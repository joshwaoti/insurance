from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from .forms import ContactForm, InsuranceForm, MyUserCreationForm, Userform
from .models import User, Client
from daraja.views import InitateSTKPush



def homePage(request):
    return render(request, 'base/home.html')


@login_required(login_url='base:login')
def dashboard(request, pk):
    user = User.objects.get(id=pk)
    client_number = user.clients.all()
    no = client_number.count()
    client = Client.objects.all()
    client_count = client.count()
    sales = client_count * 1000
    mySales = no * 1000
    client_insurance = Client.objects.filter(agent=user)
    
    # 
    # agents = User.objects.annotate(client_count=Count('clients'))
    # client_num = agents.client_count
    

    context = {
        'user' : user,
        'client_count' : client_count,
        'sales' : sales,
        'no' : no,
        'mySales' : mySales,
        'client_number' : client_number,
        
    }
    return render(request, 'base/dashboard.html', context)


def loginPage(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect('base:dashboard', pk=user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.info(request, f'You have logged in as {user.username}')
            return redirect('base:dashboard', pk=user.id)
        else:
            messages.error(request, 'Incorrect Username or password')
    return render(request, 'base/pages-login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'You have logged out successfuly!')
    return redirect('base:home')

@csrf_exempt
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, 'Account was created successfuly and you are now logged in')
            return redirect('base:dashboard', pk=user.id)

        else:
            messages.error(request, 'An error occured during registration.')

        context = {
            'form' : form,
        }

    return render(request, 'base/pages-register.html', {'form' : form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your message was sent successfully')
            return redirect ('base:home')
    form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'base/contact.html',context)

@login_required(login_url='base:login')
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
            # start_date = form.cleaned_data['start_date']
            # end_date = form.cleaned_data['end_date']
            email_subject = 'phone insurance request'
            email_message = first_name + ' ' + last_name + '\n' + email + '\n' + 'phone number: ' + phone_number + '\n' + 'imei number: ' + phone_imei + '\n' 
            # + 'start_date: ' + start_date + '\n' + 'end_date: ' + end_date

            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            user = request.user
            messages.success(request, 'You successfully registered a client for insurance')
            return redirect ('base:dashboard', pk=user.id)

    form = InsuranceForm()
    context = {
        'form': form,
    }
    return render(request, 'base/insurance.html', context)

def userProfile(request, pk):
    page = 'profile'
    user = User.objects.get(id=pk)
    context={
        'user' : user,
        'page' : page,
    }

    return render(request, 'base/users-profile.html', context)

@login_required(login_url='base:login')
def updateUser(request):
    page = 'update-user'
    user = request.user
    form = Userform(instance=user)

    if request.method == "POST":
        form = Userform(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated your profile')
            return redirect('base:profile', pk=user.id)

    context = {
        'form' : form,
        'page' : page,
    }
    return render(request, 'base/users-profile.html', context)

@login_required(login_url='base:login')
def changePassword(request):
    page = 'change-password'

    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            new_password = make_password(password1)
            request.user.password = new_password
            request.user.save()
            messages.success(request, "You successfully changed your password!")
            user = request.user
            return redirect('base:profile', pk=user.id)

    return render(request, 'base/change_password.html', {'page' : page})


def checkout(request):
    # pay = InitateSTKPush.initiate_mpesa_stk()
    return render(request, 'base/checkout.html')
