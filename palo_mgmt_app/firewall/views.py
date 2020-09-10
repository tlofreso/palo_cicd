from django.shortcuts import render, redirect
from .forms import FirewallRequestForm, FirewallRuleForm

# Create your views here.
def firewall(request):

    if request.method == "POST":
        firewallrequest_from = FirewallRequestForm(request.POST)
        firewallrule_form = FirewallRuleForm(request.POST)

        return redirect(
            request,
            "/firewall",
            {
                "firewallrequest_form": firewallrequest_from,
                "firewallrule_form": firewallrule_form,
            },
        )
    else:
        firewallrequest_from = FirewallRequestForm()
        firewallrule_form = FirewallRuleForm()
    return render(
        request,
        "firewall/firewall.html",
        {
            "firewallrequest_form": firewallrequest_from,
            "firewallrule_form": firewallrule_form,
        },
    )
