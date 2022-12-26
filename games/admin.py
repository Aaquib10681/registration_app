from django.contrib import admin

from games.models import Category, PlayerInformation

# Register your models here.
admin.site.register(Category)
admin.site.register(PlayerInformation)
