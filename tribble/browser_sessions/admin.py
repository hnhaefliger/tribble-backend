from django.contrib import admin

from .models import Session


class SessionAdmin(admin.ModelAdmin):
    fields = ('id', 'location', 'submitted_at')
    readonly_fields = ('id', 'location', 'submitted_at')

    def id(self, obj): return obj.id
    def location(self, obj): return obj.location
    def submitted_at(self, obj): return obj.submitted_at


admin.site.register(Session, SessionAdmin)
