from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as views

from music_app.album.forms import CreateAlbumForm
from music_app.album.models import Album
from music_app.web.views import get_profile


class ReadOnlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"

        return form
# Create your views here.

class CreateAlbumView(views.CreateView):
    queryset = Album.objects.all()
    #fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    template_name = "album/album-add.html"
    form_class = CreateAlbumForm
    success_url = reverse_lazy("index")

# add new album to the user's collection
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = get_profile()
        return super().form_valid(form)

    # Instead adding placeholder with help of form_class
    #def get_form(self, form_class=None):
    #   form = super().get_form(form_class=form_class)
    #   form.fields["name"].widget.attrs["placeholder] = "Album Name:"
    #   return form

class DetailAlbumView(views.DetailView):
    queryset = Album.objects.all()
    template_name = "album/album-details.html"


class EditAlbumView(views.UpdateView):
    queryset = Album.objects.all()
    template_name = "album/album-edit.html"
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    success_url = reverse_lazy('index')

class DeleteAlbumView(ReadOnlyViewMixin,views.DeleteView):
    queryset = Album.objects.all()
    template_name = "album/album-delete.html"
    fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']
    success_url = reverse_lazy('index')
    form_class = modelform_factory(
        Album,
        fields=['name', 'artist_name', 'genre', 'description', 'image_url', 'price'],
    )
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs

    def form_valid(self, form):
        form.instance = self.object
        return super().form_valid()