from django.db import models
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    title = models.CharField(_('Title'), max_length=128, db_index=True)

    class Meta:
        verbose_name = _('Page')
        default_related_name = 'pages'

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(_('Title'), max_length=128, db_index=True)
    counter = models.PositiveBigIntegerField(_('Counter'), default=0)
    page = models.ForeignKey(Page, models.SET_NULL, null=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Video(Content):
    source = models.FileField(_('File'), upload_to='videos')
    subtitles = models.FileField(_('Subtitles'), upload_to='subtitles')

    class Meta(Content.Meta):
        verbose_name = _('Video')
        default_related_name = 'videos'


class Audio(Content):
    source = models.FileField(_('File'), upload_to='audios')
    bit_rate = models.PositiveIntegerField(_('Bit rate'))

    class Meta(Content.Meta):
        verbose_name = _('Audio')
        default_related_name = 'audios'


class Text(Content):
    content = models.TextField(_('File'))

    class Meta(Content.Meta):
        verbose_name = _('Text')
        default_related_name = 'texts'
