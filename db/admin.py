from django.contrib import admin

from db.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'company', 'title', 'city', 'graduated')


# Register your models here.
admin.site.register(Contact, ContactAdmin)
