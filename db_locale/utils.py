import os
import polib

from db_locale import settings
from db_locale.models import Translation


def import_translations():
    for translate_item in settings.TRANSLATE_ITEMS:
        module_name, model_name = translate_item[0].rsplit('.', 1)
        module = __import__(module_name, fromlist=[''])
        model = getattr(module, model_name)
        items = model.objects.all()
        for item in items:
            for field in translate_item[1]:
                value = getattr(item, field, None)
                if value:
                    for language in settings.LANGUAGES:
                        if language[0] == settings.LANGUAGE_CODE:
                            continue
                        Translation.objects.get_or_create(language=language[0], msgid=value)

def import_translations_from_po():
    for language in settings.LANGUAGES:
        if language[0] == settings.LANGUAGE_CODE:
            continue
        po_file = polib.pofile(os.path.join(settings.PROJECT_ROOT, 'locale',
            language[0], 'LC_MESSAGES', 'django.po'))
        for entry in po_file:
            Translation.objects.get_or_create(language=language[0],
                msgid=entry.msgid, msgstr=entry.msgstr)

def export_translations():
    for language in settings.LANGUAGES:
        if language[0] == settings.LANGUAGE_CODE:
            continue
        translation_list = Translation.objects.filter(language=language[0])
        locale_filename = os.path.join(settings.PROJECT_ROOT, 'locale',
            language[0], 'LC_MESSAGES', 'django.po')
        po_file = polib.pofile(locale_filename)
        for translation in translation_list:
            entry = po_file.find(translation.msgid)
            if entry is not None:
                entry.msgstr = translation.msgstr
            else:
                entry = polib.POEntry(msgid=translation.msgid, msgstr=translation.msgstr)
                po_file.append(entry)
        po_file.save()
