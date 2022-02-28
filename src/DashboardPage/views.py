from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Widgets.forms import Horoscope
from .forms import ProfilOptions, SettingsOptions
from Widgets.views.views_cat import WCat
from Widgets.views.views_crypto import WCrypto
from Widgets.views.views_dehash import Dehash
from Widgets.views.views_shortener import WShortener
from Widgets.views.views_lyrics import WLyrics
from Widgets.views.views_cat import WCat
from Widgets.views.views_horoscope import WHoroscope
from Widgets.views.views_news import WNews
from DashboardPage.models import *
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login')
def DashboardPage(request):
    widgets = Widgets.objects.filter(dashboardID__userID__id=request.user.id)
    dehash = Dehash(request)
    shortener = WShortener(request)
    crypto = WCrypto(request)
    lyrics = WLyrics(request)
    cat = WCat(request)
    horoscope = WHoroscope(request)
    news = WNews(request)
    global_context = {
        "path": "Widgets/",
        "widgets": widgets,
        "dehash": dehash,
        "shortener": shortener,
        "crypto": crypto,
        "lyrics": lyrics,
        "cat": cat,
        "horoscope": horoscope,
        "news": news,
    }
    return render(request, "DashboardPage/index.html", global_context)

@login_required(login_url='/accounts/login')
def SettingsPage(request):
    dashboard = Dashboard.objects.get(userID=request.user.id)
    if request.method == "POST":
       form = SettingsOptions(request.POST)
       if form.is_valid():
           vmail = form.cleaned_data.get('mail')
           vsms = form.cleaned_data.get('sms')
           vsound = form.cleaned_data.get('sound')
           vcmode = form.cleaned_data.get('cmode')
           vdmode = form.cleaned_data.get('dmode')
           Settings.objects.filter(dashboardID=dashboard).update(mail=vmail, sms=vsms, sound=vsound, cmode=vcmode, dmode=vdmode)
    else:
        form = SettingsOptions()
    usettings = Settings.objects.get(dashboardID=dashboard)
    form = SettingsOptions(initial={'mail':usettings.mail, 'sms':usettings.sms, 'sound':usettings.sound, 'cmode':usettings.cmode, 'dmode':usettings.dmode})
    context = {
        "usettings": usettings,
        "settings": form,
        "userID": request.user.id
    }
    return render(request, "DashboardPage/settings.html", context=context)

@login_required(login_url='/accounts/login')
def ProfilePage(request):
    userID = User.objects.get(id=request.user.id)
    if request.method == "POST":
       form = ProfilOptions(request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           lastname = form.cleaned_data.get('lastname')
           firstname = form.cleaned_data.get('firstname')
           email = form.cleaned_data.get('email')
           phone = form.cleaned_data.get('phone')
           address = form.cleaned_data.get('address')
           city = form.cleaned_data.get('city')
           country = form.cleaned_data.get('country')
           User.objects.filter(id=request.user.id).update(username=username, last_name=lastname,
           first_name=firstname, email=email)
           UserInfos.objects.filter(userID=userID).update(phone=phone, address=address, city=city,
           country=country)
    else:
        form = UserInfos()
    me = User.objects.get(id=request.user.id)
    userInfos = UserInfos.objects.get(userID=me)
    form = ProfilOptions(initial={'username': me.username, 'lastname': me.last_name,
    'email': me.email, 'firstname': me.first_name,
    'phone': userInfos.phone, 'address': userInfos.address,
    'city': userInfos.city, 'country': userInfos.country})
    context = {
        "user": me,
        "userInfos": userInfos,
        "form": form
    }
    return render(request, "DashboardPage/profile.html", context=context)


@login_required(login_url='/accounts/login')
def NavbarPage(request):
    return render(request, "DashboardPage/navbar.html")

@login_required(login_url='/accounts/login')
def ShopPage(request):
    widgets = Widgets.objects.all()
    winstalled = Widgets.objects.filter(dashboardID__userID__id=request.user.id)
    context = {
        "widgets" : widgets,
        "winstalled": winstalled,
    }
    return render(request, "DashboardPage/shop.html", context=context)

@login_required(login_url='/accounts/login')
def InstallWidget(request, id):
    widget = Widgets.objects.get(id=id)
    dashboard = Dashboard.objects.filter(userID__id=request.user.id)[0]
    widget.dashboardID.add(dashboard)
    return redirect("ShopPage")

@login_required(login_url='/accounts/login')
def UninstallWidget(request, id):
    widget = Widgets.objects.get(id=id)
    dashboard = Dashboard.objects.filter(userID__id=request.user.id)[0]
    widget.dashboardID.remove(dashboard)
    return redirect("ShopPage")

@login_required(login_url='/accounts/login')
def DeleteUser(request, id):
    if (request.user.id == id):
        u = User.objects.get(id=id)
        u.delete()
        return redirect("LogoutPage")
    return redirect("SettingsPage")

@login_required(login_url='/accounts/login')
def RunWidget(request, name):
    return redirect("DashboardPage")
