from django.contrib import admin
from django.contrib.admin import register
from django.utils.translation import gettext_lazy as _

from content.models import Page, PageContentTypes, Video, Audio, Text


class ContentInline(admin.TabularInline):
    readonly_fields = ('counter',)
    extra = 1


class VideoInline(ContentInline):
    model = Video


class AudioInline(ContentInline):
    model = Audio


class TextInline(ContentInline):
    model = Text


@register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] + PageContentTypes.values
    search_fields = ('title',)
    list_filter = ('title',)
    inlines = (VideoInline, AudioInline, TextInline)

    def videos(self, obj):
        return str(obj.videos.count())
    videos.short_description = _('Videos')

    def audios(self, obj):
        return str(obj.audios.count())
    audios.short_description = _('Audios')

    def texts(self, obj):
        return str(obj.texts.count())
    texts.short_description = _('Texts')


class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'page')
    list_filter = ('page',)
    search_fields = ('title',)


@register(Video)
class VideoAdmin(ContentAdmin):
    pass


@register(Audio)
class AudioAdmin(ContentAdmin):
    pass


@register(Text)
class TextAdmin(ContentAdmin):
    search_fields = ('title', 'content')
