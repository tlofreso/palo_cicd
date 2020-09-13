from django.contrib import admin
from firewall.models import FirewallRequest, FirewallRule

# Register your models here.
admin.site.register(FirewallRequest)
admin.site.register(FirewallRule)
