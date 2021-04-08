from django.contrib import admin

# Register your models here.
from .models import User_detail,Nominance,Party

admin.site.register(User_detail)
admin.site.register(Nominance)
admin.site.register(Party)