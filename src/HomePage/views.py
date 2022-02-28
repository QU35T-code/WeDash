from django.shortcuts import render, redirect

def HomePage(request):
    if request.user.is_authenticated:
        return redirect("DashboardPage")
    return render(request, "HomePage/index.html")
