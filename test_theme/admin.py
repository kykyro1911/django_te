from django.contrib import admin
from .models import Users, ex_excel


class YourAdmin(admin.ModelAdmin):
    # readonly_fields = ('save_date', 'mod_date',)
    list_display = ('Name', 'Position','Office', 'Age', 'Start_date', 'Salary')

admin.site.register(ex_excel, YourAdmin)
admin.site.register(Users)
