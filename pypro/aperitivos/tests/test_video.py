import pytest
from django.urls import reverse
from model_mommy import mommy

from pypro.aperitivos.models import Video
from pypro.django_assertions import assert_contains


@pytest.fixture
def video(db):
    return mommy.make(Video)


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=('motivacao',)))


@pytest.fixture
def resp_video_nao_encontrado(client, video):


    return client.get(reverse('aperitivos:video', args=(video.slug + 'video não encontrado',)))


def test_status_code_video_nao_encontrado(resp_video_nao_encontrado):


    assert resp_video_nao_encontrado.status_code == 404


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video=None):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp):
    assert_contains(resp, '<iframe src="https://player.vimeo.com/video/730872873?h=a14e61ba65&amp;badge=0&amp'
                          ';autopause=0&amp;player_id=0&amp;app_id=58479" ')