from django.contrib import admin

# Register your models here.
from LMS_App.models import Book,Register

admin.site.register(Book)
admin.site.register(Register)
