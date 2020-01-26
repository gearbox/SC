from django.contrib import admin
from .models import SCPoint, SCType, Message, Method
# Register your models here.


admin.site.register(SCPoint)
admin.site.register(SCType)
admin.site.register(Message)
admin.site.register(Method)
