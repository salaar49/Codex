from django.contrib import admin
from .models import Category, Course, SubCategory

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(SubCategory)