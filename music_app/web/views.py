import django.forms as forms
from django.shortcuts import render, redirect

from music_app.album.models import Album
from music_app.profile.models import Profile
from music_app.web.forms import CreateProfileForm


# Create your views here.
def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            profile = form.save()
            return redirect("index")

    context = {
            "form": form
        }

    return render(request, "web/home-no-profile.html", context)

def index_with_profile(request):
    pass

def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)
    context = {
        "albums": Album.objects.all()
    }
    return render(request, "web/home-with-profile.html", context)