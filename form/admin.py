from django.contrib import admin
from .views import User, Event, Round
# Register your models here.

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Round)