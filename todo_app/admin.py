from django.contrib import admin

# Register your models here.
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Todo, TodoAdmin)