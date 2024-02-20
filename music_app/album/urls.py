from django.urls import path

from music_app.album.views import CreateAlbumView, DetailAlbumView, EditAlbumView, DeleteAlbumView

urlpatterns = [
    path('add/', CreateAlbumView.as_view(), name='create_album'),
    path('<int:pk>/details/', DetailAlbumView.as_view(), name='details_album'),
    path('<int:pk>/edit', EditAlbumView.as_view(), name='edit_album'),
    path('<int:pk>/delete/', DeleteAlbumView.as_view(), name='delete_album')
]