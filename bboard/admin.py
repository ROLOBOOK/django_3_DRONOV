from django.contrib import admin

# Register your models here.

from .models import Bd
from .models import Rubric


class BdAdmib(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')


admin.site.register(Bd, BdAdmib)
admin.site.register(Rubric)
