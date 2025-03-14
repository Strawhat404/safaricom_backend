from django.contrib import admin
from .models import Bank, Branch, Application

admin.site.register(Bank)
admin.site.register(Branch)
admin.site.register(Application)