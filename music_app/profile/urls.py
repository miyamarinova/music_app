from django.urls import path

from music_app.profile.views import DetailProfileView, DeleteProfileView

urlpatterns=[
    path('details/', DetailProfileView.as_view(), name='detail_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile')
]