from django.contrib import admin
from .models import user_login,user_details,user_query
# Register your models here.
admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(user_query)

