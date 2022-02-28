from django.shortcuts import  render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from DashboardPage.models import *
from Accounts.forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm

def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect("DashboardPage")
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			dashboard_obj = Dashboard(name=user.username + " Dashboard", userID=user)
			dashboard_obj.save()
			dashboard_ID = Dashboard.objects.get(userID=user)
			settings_obj = Settings(dashboardID=dashboard_ID)
			settings_obj.save()
			userInfos = UserInfos(userID=user)
			userInfos.save()
			return redirect("HomePage")
		else:
			messages.error(request, "A user with that username already exists.")
			return render(request=request, template_name="Accounts/register.html", context={"register_form":form})
	else:
		form = NewUserForm()
		return render(request=request, template_name="Accounts/register.html", context={"register_form":form})

def LoginPage(request):
	if request.user.is_authenticated:
		return redirect("DashboardPage")
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				redirect_param = request.GET.getlist('next')
				if not redirect_param:
					return redirect("DashboardPage")
				return redirect(redirect_param[0])
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="Accounts/login.html", context={"login_form":form})

def LogoutPage(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("HomePage")
