from django.contrib import messages
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render, redirect
from django.conf import settings
from emailnotification.forms import SubscribeForm
def subscribe(request):
    form = SubscribeForm()
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            subject = 'wishes'
            message = 'hello'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'mail sent successfully')
            return redirect('subscribe')
    return render(request, 'home.html', {'form': form})