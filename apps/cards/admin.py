from django.contrib import admin

from .models import Title, Contact, BankRequisites


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'icon',
        'url',
    )
    search_fields = (
        'url',
    )


@admin.register(BankRequisites)
class BankRequisitesAdmin(admin.ModelAdmin):
    list_display = (
        'requisites',
        'image',
    )
    search_fields = (
        'requisites',
    )
