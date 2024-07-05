from django.urls import path
from .views import upload_song,home, song_list

urlpatterns = [
    path('',home,name='home'),
    path('upload/', upload_song, name='upload_song'),
    path('songs/', song_list, name='song_list')
]