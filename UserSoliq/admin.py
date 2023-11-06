from django.contrib import admin
from .models import *

admin.site.site_header = "Soliquz Admin"
admin.site.register(UserModel)

