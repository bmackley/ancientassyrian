from django.db import models
from django.contrib import admin
from .models import *

# register any models here
admin.site.register(User)
admin.site.register(Tablet)
admin.site.register(Line)
admin.site.register(AssyrianChar)
admin.site.register(Sign)
admin.site.register(IdentifiedCharacter)
