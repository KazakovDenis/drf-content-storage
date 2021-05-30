from django.db import models, transaction
from django.db.models import F
from django.utils.translation import gettext_lazy as _


class PageContentTypes(models.TextChoices):
    VIDEO = 'videos', _('Videos')
    AUDIO = 'audios', _('Audios')
    TEXT = 'texts', _('Texts')


class Page(models.Model):
    title = models.CharField(_('Title'), max_length=128, db_index=True)

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _('Pages')
        default_related_name = 'pages'

    def increment_counters(self):
        """Increment counters of this page contents"""
        for content_type in PageContentTypes.values:
            content = getattr(self, content_type)
            with transaction.atomic():
                content.select_for_update().update(counter=F('counter') + 1)

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
        verbose_name_plural = _('Videos')
        default_related_name = 'videos'


class Audio(Content):
    source = models.FileField(_('File'), upload_to='audios')
    bit_rate = models.PositiveIntegerField(_('Bit rate'))

    class Meta(Content.Meta):
        verbose_name = _('Audio')
        verbose_name_plural = _('Audios')
        default_related_name = 'audios'


class Text(Content):
    content = models.TextField(_('Content'))

    class Meta(Content.Meta):
        verbose_name = _('Text')
        verbose_name_plural = _('Texts')
        default_related_name = 'texts'
