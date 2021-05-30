from django.urls import path

from .views import api_root, PageAPIView, VideoAPIView, AudioAPIView, TextAPIView

app_name = 'api'

urlpatterns = [
    path('', api_root, name='root'),
    path('pages/', PageAPIView.as_view({'get': 'list'}), name='page-list'),
    path('pages/<int:pk>/', PageAPIView.as_view({'get': 'retrieve'}), name='page-detail'),

    path('videos/', VideoAPIView.as_view({'get': 'list'}), name='video-list'),
    path('videos/<int:pk>/', VideoAPIView.as_view({'get': 'retrieve'}), name='video-detail'),

    path('audios/', AudioAPIView.as_view({'get': 'list'}), name='audio-list'),
    path('audios/<int:pk>/', AudioAPIView.as_view({'get': 'retrieve'}), name='audio-detail'),

    path('texts/', TextAPIView.as_view({'get': 'list'}), name='text-list'),
    path('texts/<int:pk>/', TextAPIView.as_view({'get': 'retrieve'}), name='text-detail'),
]
