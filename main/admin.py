from django.contrib import admin
from .models import cardRecipient, CustomUser

admin.site.register(cardRecipient)
admin.site.register(CustomUser)