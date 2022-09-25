from django.contrib import admin
from .models import Gender,Director,Movie
# Register your models here.

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Gender)
