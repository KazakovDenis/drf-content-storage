import pytest


@pytest.fixture
def api_get(client):
    """A shortcut to send GET requests"""
    def send(url, query_params=None):
        return client.get(url, data=query_params, content_type='application/json')
    return send


@pytest.fixture
def page(mixer):
    return mixer.blend('content.Page', id=1)


@pytest.fixture
def all_content(mixer, page):
    return (
        mixer.blend('content.Video', id=1, page=page),
        mixer.blend('content.Audio', id=1, page=page),
        mixer.blend('content.Text', id=1, page=page),
    )
