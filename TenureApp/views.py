from django.http import HttpResponse
from django.shortcuts import render

from .forms import AssetForm
from .models import Assets
# Create your views here.

def homepage(request):
    # return HttpResponse("Homepage")
    asset_list = Assets.objects.all()
    return render(request, 'homepage.html', {"asset_list" : asset_list})

def publish(request):
    if request.method == "POST":
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Form request is valid")
    else:
        form = AssetForm()
    return render(request, "publish.html", {"form" : form})