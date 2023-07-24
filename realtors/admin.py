from django.contrib import admin

# Register your models here.

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email','hire_date', 'is_mvp')
  list_editable = ('is_mvp',)
  list_display_list = ('id', 'name',)
  list_display_links = ('id','name')
  search_fields =('name',)
  list_per_page = 20

admin.site.register(Realtor,RealtorAdmin)