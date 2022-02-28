from django.db import models
from django.contrib.auth.models import User

class UserInfos(models.Model):
    id = models.IntegerField(primary_key=True)
    phone = models.CharField(null=True, default="", max_length=15)
    address = models.CharField(null=True, default="", max_length=100)
    city =  models.CharField(null=True, default="", max_length=50)
    country = models.CharField(null=True, default="", max_length=50)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Dashboard(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=20, default="Dashboard")
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    description = models.TextField(null=False, max_length=100)

class Widgets(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(null=False, max_length=20)
    slug = models.SlugField(max_length=20, null=False)
    description = models.TextField(null=False, max_length=100)
    need_auth = models.BooleanField(null=False, default=False)
    positionColumn = models.IntegerField(null=True)
    positionRow = models.IntegerField(null=True)
    sizeColumn = models.IntegerField(null=True)
    sizeRow = models.IntegerField(null=True)
    rate = models.IntegerField(default=0, null=False)
    img = models.URLField(max_length=200, null=False)
    dashboardID = models.ManyToManyField(Dashboard)
    catID = models.ForeignKey(Categories, on_delete=models.CASCADE)

class Opinion(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    rate = models.IntegerField(null=False)
    description = models.TextField(max_length=200, null=False)
    date = models.DateField(auto_now_add=True, null=False)
    widgetID = models.ForeignKey(Widgets, on_delete=models.CASCADE)

class Settings(models.Model):
    id = models.IntegerField(primary_key=True)
    mail = models.BooleanField(default=False)
    sms = models.BooleanField(default=False)
    sound = models.BooleanField(default=False)
    cmode = models.BooleanField(default=False)
    dmode = models.BooleanField(default=False)
    lang = models.CharField(default="French", max_length=20)
    dashboardID = models.ForeignKey(Dashboard, on_delete=models.CASCADE)