import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


class TestAPIViews:

    @pytest.mark.parametrize('view_name', [
        'api:page-list',
        'api:video-list',
        'api:audio-list',
        'api:text-list',
    ])
    @pytest.mark.usefixtures('all_content')
    def test_api_urls_list_200(self, api_get, view_name):
        response = api_get(reverse(view_name))
        assert response.status_code == 200
        response = response.json()
        assert len(response.get('results')) == 1

    @pytest.mark.parametrize('view_name, args', [
        ('api:page-detail', [1]),
        ('api:video-detail', [1]),
        ('api:audio-detail', [1]),
        ('api:text-detail', [1]),
    ])
    @pytest.mark.usefixtures('all_content')
    def test_api_urls_detail_200(self, api_get, view_name, args):
        url = reverse(view_name, args=args)
        response = api_get(url)
        assert response.status_code == 200
        response = response.json()
        assert response.get('id') == 1
