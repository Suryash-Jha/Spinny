from django.contrib import admin

# Register your models here.

from .models import BoxModel, customUser, constraints
from rest_framework.authtoken.admin import TokenAdmin

# import token also


admin.site.register(BoxModel)
admin.site.register(customUser)
admin.site.register(constraints)




