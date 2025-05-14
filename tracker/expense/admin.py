from django.contrib import admin
from expense.models import *


admin.site.site_header="Expence tracker"
admin.site.site_title="Expence tracker"
admin.site.site_url="Expence tracker"
admin.site.register(CurrentBalance)

class TrackingHistoryAdmin(admin.ModelAdmin):
       list_display=[
                "amount",
                "current_balance",
                "description",
                "expence_type",
                "created_at"
       ]
       search_fields=[
           "expence_type",
           "description"
       ]

admin.site.register(TrackingHistory,TrackingHistoryAdmin)