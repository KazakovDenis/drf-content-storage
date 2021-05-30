from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet

from content.models import Page, Video, Audio, Text
from content.serializers import PageSerializer, VideoSerializer, AudioSerializer, TextSerializer
from content.tasks import increment_content_counters


@api_view(['GET'])
def api_root(request, format=None):    # noqa
    return Response({
        'pages': reverse('api:page-list', request=request, format=format),
        'content': {
            'video': reverse('api:video-list', request=request, format=format),
            'audio': reverse('api:audio-list', request=request, format=format),
            'text': reverse('api:text-list', request=request, format=format),
        },
    })


class PageAPIView(ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, *args, **kwargs):
        """Increment content counters while retrieving page details"""
        page = self.get_object()
        increment_content_counters.apply_async((page.id,))
        return super().retrieve(request, *args, **kwargs)


class VideoAPIView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class AudioAPIView(ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer


class TextAPIView(ModelViewSet):
    queryset = Text.objects.all()
    serializer_class = TextSerializer
