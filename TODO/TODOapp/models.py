from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#title, status, date-current, user,priority------------->


class TODO(models.Model):
    status_choices = [
        ('C','completed'),
        ('P','pending')
    ]
    priority_choices = [
        ('1', 'top priority'),
        ('2', 'high priority'),
        ('3', 'medium'),
        ('4', 'low'),
        ('5', 'hold')

    ]
    title = models.CharField(max_length = 30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=status_choices)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=5, choices=priority_choices)

