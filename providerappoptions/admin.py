from django.contrib import admin
from .models import MainApp, AppSubType, AppHosting, ListingStatus, ListingAppStatus, ListingStateStatus


class MainAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'is_active')
    search_fields = ('name', 'value')


class AppSubTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'main_app', 'is_active')
    search_fields = ('name', 'value')
    list_filter = ('main_app',)


class AppHostingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'subtype', 'is_active')
    search_fields = ('name', 'value')
    list_filter = ('subtype',)


class ListingStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')
    search_fields = ('name', 'value')


class ListingAppStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')
    search_fields = ('name', 'value')

class ListingStateStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')
    search_fields = ('name', 'value')


admin.site.register(MainApp, MainAppAdmin)
admin.site.register(AppSubType, AppSubTypeAdmin)
admin.site.register(AppHosting, AppHostingAdmin)
admin.site.register(ListingStatus, ListingStatusAdmin)
admin.site.register(ListingAppStatus, ListingAppStatusAdmin)
admin.site.register(ListingStateStatus, ListingStateStatusAdmin)