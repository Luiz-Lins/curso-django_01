# from pyclbr import Class

# from django.db import models
from django.shortcuts import render
from django.urls import reverse

# from pypro.aperitivos.models import Video


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='730872873'),
    Video(slug='instalacao-windows', titulo='Instalação Windows', vimeo_id='731597193'),
]

videos_dct = {v.slug: v for v in videos}


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
