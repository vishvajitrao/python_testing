from django.contrib import admin
from django.db.models.fields import SmallIntegerField
from api.models import *
from simple_history.admin import SimpleHistoryAdmin


# foreign key
admin.site.register(Reporter)
admin.site.register(Article)

# foreign key
admin.site.register(Poll)
admin.site.register(Choice)

# one to one 
admin.site.register(Student)
admin.site.register(College)


# Add custom fields in History Model
# class ChoiceHistoryAdmin(SimpleHistoryAdmin):
#     history_list_display = ["status", "ip_address"]
# admin.site.register(Choice, ChoiceHistoryAdmin)



