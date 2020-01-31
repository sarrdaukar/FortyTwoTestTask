from django.contrib import admin

from apps.hello.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
