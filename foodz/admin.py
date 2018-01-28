from django.contrib import admin
from .models import Recipe
from .models import User
from .models import History

admin.site.register(Recipe)
admin.site.register(User)
admin.site.register(History)

# Register your models here.
