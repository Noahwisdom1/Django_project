from django.contrib import admin
from . models import Member, Meta

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'country')

class MetaAdmin(admin.ModelAdmin):
    list_display = ('car', 'country', 'release_date')

admin.site.register(Member, MemberAdmin)
admin.site.register(Meta, MetaAdmin)