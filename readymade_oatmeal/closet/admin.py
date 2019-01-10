from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Clothes)
admin.site.register(models.Photo)

