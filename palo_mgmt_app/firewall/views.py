from django.shortcuts import render, redirect

# Create your views here.
def firewall(request):
    return render(request, "firewall/firewall.html")
