from django.forms import ModelForm
from firewall.models import FirewallRequest, FirewallRule


class FirewallRequestForm(ModelForm):
    class Meta:
        model = FirewallRequest
        fields = "__all__"


class FirewallRuleForm(ModelForm):
    class Meta:
        model = FirewallRule
        fields = "__all__"

