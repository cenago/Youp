from django.contrib import admin

# Register your models here.
from .models import CustDtil, DriverDtil,Request_id

admin.site.register(CustDtil)
admin.site.register(DriverDtil)
admin.site.register(Request_id)
