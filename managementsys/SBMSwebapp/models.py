from django.db import models
from django.contrib.auth.models import user


# Create your models here.
class CalEvent(models.Mobels):
    who = models.CharField(max_length = 200)
    service = models.CharField(max_length = 200)
    when = models.DateTimeField(null=True, blank = True)
    cost = models.DecimalField(null = True, blank = True, max_digits=4)

class Professional(models.Models):
    name = models.OneToOneField(user.name,on_delete=models.CASCADE)
    email = models.OneToOneField(user.email,on_delete=models.CASCADE)
    summary = models.ForeignKey(CalEvent,on_delete=models.CASCADE)
