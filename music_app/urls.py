from django.contrib import admin
from django.urls import path, include
from music_app.common.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('music_app.album.urls')),
    path('profile/', include('music_app.profile.urls')),

    path('', home_page, name='home page')
]

