from django.contrib import admin
from .models import Contact, Client, User

admin.site.site_header = 'Device Solutions Hub Admin'

admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(User)