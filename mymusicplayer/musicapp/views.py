from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song

def home(request):
    return render(request, 'home.html')

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after successful upload
    else:
        form = SongForm()
    return render(request, 'upload_song.html', {'form': form})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html',{'songs': songs})