import json

from django.contrib import admin
from django.db.models import Count
from django.db.models.functions import TruncDay
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.models import Group


from .models import User
from .actions import demote, promote

# sv002
admin.site.site_header = "SaVests User Management"


demote.short_description = "Make selected users Juniors"
promote.short_description = "Make selected users Seniors"
# send_email.short_description = "Write to selected users"


# sv005
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('first_name', 'last_name', 'password', 'last_login',
               'groups', 'user_permissions')

    fields = (('name', 'username', 'email',),
              ('department', 'level', 'date_joined',),
              ('is_superuser', 'is_staff', 'is_active',),)

    list_display = ('name', 'email', 'department', 'level', 'is_active',)
    list_filter = ('date_joined', 'department', 'level',)
    list_editable = ('is_active',)
    list_per_page = 15
    actions = [promote, demote]
    actions_on_top = False
    actions_on_bottom = True
    empty_value_display = 'Unavailable'
    readonly_fields = ('date_joined',)

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        chart_data = (
            User.objects.annotate(date=TruncDay("date_joined"))
            .values("date")
            .annotate(y=Count("id"))
            .order_by("-date")
        )

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


admin.site.unregister(Group)
