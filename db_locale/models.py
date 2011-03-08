from django.db import models

TS_NONTRANSLATED, TS_TRANSLATED = 0, 1

TRANSLATION_STATUS_CHOICES = (
    (TS_NONTRANSLATED, "Non-translated"),
    (TS_TRANSLATED, "Translated"),
)

class Translation(models.Model):

    language = models.CharField(max_length=255)
    msgid = models.TextField()
    msgstr = models.TextField(default="", blank=True)
    status = models.IntegerField(choices=TRANSLATION_STATUS_CHOICES, default=TS_NONTRANSLATED)
