from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import random , string

# Create your views here.


def randomurl():

    while True:

        short_code = "".join(random.choice(string.ascii_lowercase)for _ in range(6))

        if not Shorturl.objects.filter(short_url = short_code).exists():
            return short_code



def home(request):

    if request.method == "POST":

        if request.POST["original"]:

            original_url = request.POST.get("original")

            if not original_url.startswith(('https://' , 'http://')):
                original_url ='https://www.' + original_url


            short_url = randomurl()


            url = Shorturl.objects.create(
                        original_url = original_url,
                        short_url = short_url,
                    )

            url.save()
           

            return render(request , 'home.html' , {'url':url})
        
    return render(request , 'home.html')

def redirect_url(request , short_code):

    original = Shorturl.objects.get(short_url = short_code)

    return redirect(original.original_url)




