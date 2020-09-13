from django.shortcuts import render, redirect
from .forms import FirewallRequestForm, FirewallRuleForm
from .models import FirewallRule

# Create your views here.
def firewall(request):

    if request.method == "POST":
        firewallrequest_from = FirewallRequestForm(request.POST)
        firewallrule_form = FirewallRuleForm(request.POST)

        if firewallrequest_from.is_valid() and firewallrule_form.is_valid():
            r = firewallrequest_from.save()

            firewallrequest = r.request_id
            source_ip = firewallrule_form["source_ip"].cleaned_data()
            source_host = firewallrule_form["source_host"].cleaned_data()
            source_port = firewallrule_form["source_port"].cleaned_data()
            destination_ip = firewallrule_form["destination_ip"].cleaned_data()
            destination_host = firewallrule_form["destination_host"].cleaned_data()
            destination_port = firewallrule_form["destination_port"].cleaned_data()
            protocol = firewallrule_form["destination_protocol"].cleaned_data()

            rule = FirewallRule(
                firewallrequest=firewallrequest,
                source_ip=source_ip,
                source_host=source_host,
                source_port=source_port,
                destination_ip=destination_ip,
                destination_host=destination_host,
                destination_port=destination_port,
                protocol=protocol,
            )
            rule.save()

            return redirect(
                request,
                "/firewall.html",
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
