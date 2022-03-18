from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(tags)
admin.site.register(Comment)
admin.site.register(Ratings)

