from django.contrib import admin
from .models import Player,GK,DEF,MID,FWRD,Teams
# Register your models here.

admin.site.register(Player)
admin.site.register(GK)
admin.site.register(DEF)
admin.site.register(MID)
admin.site.register(FWRD)
admin.site.register(Teams)