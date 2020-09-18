from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# class Professional(models.Model):
#     name = models.ForeignKey(User.first_name,on_delete=models.CASCADE)
#     name = models.User.first_name
#     email = models.ForeignObject(User.email,on_delete=models.CASCADE)
#     summary = models.ForeignKey(CalEvent,on_delete=models.CASCADE)

class CalEvent(models.Model):
    who = models.CharField(max_length = 200)
    service = models.CharField(max_length = 200)
    when = models.DateTimeField(null=True, blank = True)
    cost = models.DecimalField(null = True, blank = True, max_digits=4, decimal_places=2)
    professional = models.ForeignKey( get_user_model(), on_delete=models.CASCADE)


