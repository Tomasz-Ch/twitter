from django.contrib import admin

# Register your models here.

from twitter import models

admin.site.register(models.Tweet)
