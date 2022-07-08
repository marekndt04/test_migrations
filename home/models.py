from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page


class HomePage(Page):
    pass


class NewModel(Page):
    second_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    footer = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("second_title"),
        FieldPanel("description"),
        FieldPanel("footer"),
    ]
