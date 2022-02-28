from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render

from SupportPage.models import Support
from .forms import ContactForm
from django.conf import settings as conf_settings

@login_required(login_url='/accounts/login')
def SupportPage(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = request.user.email
            number_of_tickets = Support.objects.all().count()
            full_subject = subject + str(number_of_tickets) + " --"
            new_entry = Support(subject=full_subject, message=message, mail=email)
            new_entry.save()
            full_message = message
            try:
                send_mail(full_subject, full_message, conf_settings.DEFAULT_FROM_EMAIL, [conf_settings.DEFAULT_SEND_EMAIL])
                send_mail(full_subject, full_message, conf_settings.DEFAULT_FROM_EMAIL, [email])
            except BadHeaderError:
                return HttpResponse('Error mail send')
            form = ContactForm()
            return render(request, 'SupportPage/index.html', {'form': form, "infos" : "Your request has been sent. You will receive a recap in the next few minutes."})
    return render(request, "SupportPage/index.html", {'form': form})