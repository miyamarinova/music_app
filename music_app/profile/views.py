from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from music_app.profile.models import Profile


def get_profile():
    return Profile.objects.first()

# Create your views here.
class DetailProfileView(views.DetailView):
    queryset = Profile.objects.all()
    template_name = 'profile/profile-details.html'
    def get_object(self, queryset=None):
        return get_profile()


class DeleteProfileView(views.DeleteView):
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile()