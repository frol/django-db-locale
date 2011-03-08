from django.conf import settings

PROJECT_ROOT = settings.PROJECT_ROOT
TRANSLATE_ITEMS = getattr(settings, 'DB_LOCALE_TRANSLATE_ITEMS', tuple())
LANGUAGES = getattr(settings, 'LANGUAGES', tuple())
LANGUAGE_CODE = getattr(settings, 'LANGUAGE_CODE', 'en')
