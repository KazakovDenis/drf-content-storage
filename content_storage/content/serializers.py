from rest_framework import serializers

from content.models import Page, Video, Audio, Text


class ContentSerializer(serializers.ModelSerializer):
    page = serializers.HyperlinkedIdentityField(view_name='api:page-detail')


class VideoSerializer(ContentSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'counter', 'source', 'subtitles', 'page')


class AudioSerializer(ContentSerializer):
    class Meta:
        model = Audio
        fields = ('id', 'title', 'counter', 'source', 'bit_rate', 'page')


class TextSerializer(ContentSerializer):
    class Meta:
        model = Text
        fields = ('id', 'title', 'counter', 'content', 'page')


class PageSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:page-detail')
    videos = VideoSerializer(many=True)
    audios = AudioSerializer(many=True)
    texts = TextSerializer(many=True)

    class Meta:
        model = Page
        fields = ('url', 'title', 'videos', 'audios', 'texts')
