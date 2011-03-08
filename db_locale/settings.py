from django.conf import settings

LOCALE_ROOT = settings.LOCALE_ROOT
TRANSLATE_ITEMS = getattr(settings, 'DB_LOCALE_TRANSLATE_ITEMS', tuple())
LANGUAGES = getattr(settings, 'LANGUAGES', tuple())
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')
