from django.contrib import admin
from .models import SCPoint, Type, Message, Language
# Register your models here.


admin.site.register(SCPoint)
admin.site.register(Type)
admin.site.register(Message)
admin.site.register(Language)
