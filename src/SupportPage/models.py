from django.db import models

class Support(models.Model):
    ticket_id = models.IntegerField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    subject = models.CharField(null=False, max_length=20)
    message = models.TextField(null=False, max_length=100)
    mail = models.EmailField(null=False)