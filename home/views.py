from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from home.forms import ContactForm
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {
        'settings': Setting.objects.filter(status="True").last(),
        'content': Home.objects.filter(status="True"),
        'links': Social.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'skills': Skills.objects.all(),
        'awards': AwardAndCertifica.objects.all(),
    }
    return render(request, 'home/index.html', context)


@login_required()
def delete_profile(request, id):
    profile = get_object_or_404(Home, id=id)
    try:
        profile.delete()
        messages.success(request, "Profile deleted.")
    except:
        messages.error(request, "Profile not deleted.")

    return redirect('home:index')


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            contact = form.save()
            contact.ip = request.META.get('REMOTE_ADDR')
            url = request.META.get('HTTP_REFERER')
            contact.save()
            messages.success(request, 'Message sent.')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, 'Message could not be sent.')

    context = {'form': form,
               'content': Home.objects.filter(status="True"),
               }

    return render(request, 'home/contact.html', context)
