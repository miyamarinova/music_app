from django import forms
from music_app.album.models import Album

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['name', 'artist_name', 'genre', 'description', 'image_url', 'price']

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Album Name"
                }
            ),
            "artist_name": forms.TextInput(
                attrs={
                    "placeholder": "Artist Name"
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "placeholder": "Description"
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "placeholder": "Image URL"
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "placeholder": "Price"
                }
            )
        }
