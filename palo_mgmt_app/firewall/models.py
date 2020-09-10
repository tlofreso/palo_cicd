from django.db import models
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator

PROTOCOL_CHOICES = [("ICMP", "ICMP"), ("TCP", "TCP"), ("UDP", "UDP")]

# Defines the structure of a new firewall request
class FirewallRequest(models.Model):
    request_id = models.CharField(max_length=20)
    requestor = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    request_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(blank=True)
    justification = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)


# Defines the rules (IP/Port/Protocol) for the firewall request
class FirewallRule(models.Model):
    record = models.ForeignKey("FirewallRequest", on_delete=models.CASCADE)
    source_ip = models.GenericIPAddressField()
    source_host = models.CharField(max_length=30)
    source_port = models.PositiveIntegerField(
        validators=[MaxValueValidator(65535), MinValueValidator(1)]
    )
    destination_ip = models.GenericIPAddressField()
    destination_host = models.CharField(max_length=30)
    destination_port = models.PositiveIntegerField(
        validators=[MaxValueValidator(65535), MinValueValidator(1)]
    )
    protocol = models.CharField(max_length=(4), choices=PROTOCOL_CHOICES)

