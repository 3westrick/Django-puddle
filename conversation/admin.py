from django.contrib import admin
from .models import Conversation, ConvMessage
# Register your models here.
admin.site.register(Conversation)
admin.site.register(ConvMessage)
