from django.contrib import admin
from . models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'password', 'is_teacher')
    exclude = ('id',)

class MarksheetAdmin(admin.ModelAdmin):
    list_display = ('grade','english', 'science', 'maths','user')
    exclude = ('id',)

admin.site.register(User, UserAdmin)
admin.site.register(Marksheet, MarksheetAdmin)