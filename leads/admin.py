from django.contrib import admin
from .models import Lead, SalesAgents, User

# Register your models here.
admin.site.register(Lead)
admin.site.register(SalesAgents)
admin.site.register(User)