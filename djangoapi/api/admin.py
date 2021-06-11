from django.contrib import admin
from django.db.models.fields import SmallIntegerField
from api.models import *
from simple_history.admin import SimpleHistoryAdmin


# admin.site.register(Reporter)
# admin.site.register(Article)
admin.site.register(Poll, SimpleHistoryAdmin)

class ChoiceHistoryAdmin(SimpleHistoryAdmin):
    history_list_display = ["status", "ip_address"]


admin.site.register(Choice, ChoiceHistoryAdmin)


# Register your models here.
