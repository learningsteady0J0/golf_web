from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def get_video(request, video_name):
    video_path = os.path.join(settings.MEDIA_ROOT, video_name)
    return FileResponse(open(video_path, 'rb'), content_type='video/mp4')