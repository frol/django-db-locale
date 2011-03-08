from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.views.generic.simple import direct_to_template

from db_locale import settings
from db_locale.models import Translation, TS_NONTRANSLATED, TS_TRANSLATED
from db_locale.utils import import_translations, export_translations

@staff_member_required
def language_list(request, template_name="db_locale/language_list.html"):
    return direct_to_template(request, template_name, {
            'default_language': settings.LANGUAGE_CODE,
            'language_list': settings.LANGUAGES,
        })

@staff_member_required
def translation_list(request, language, status, template_name="db_locale/translation_list.html"):
    if request.method == 'POST':
        for item in request.POST.items():
            pack = item[0].rsplit('_', 1)
            if len(pack) != 2:
                continue
            field_name, id = pack
            if field_name == 'msgstr':
                try:
                    translation = Translation.objects.get(id=id)
                except Translation.DoesNotExists:
                    continue
                if item[1] == "" or item[1] == " ":
                    translation.status = TS_NONTRANSLATED
                else:
                    translation.status = TS_TRANSLATED
                translation.msgstr = item[1]
                translation.save()

    translation_list = Translation.objects.filter(language=language)
    if status == 'nontrans':
        translation_list = translation_list.filter(status=TS_NONTRANSLATED)
    return direct_to_template(request, template_name, {
            'language': language,
            'status': status,
            'translation_list': translation_list
        })

@staff_member_required
def refresh_request(request):
    import_translations()
    return redirect('db_locale_language_list')

@staff_member_required
def apply_request(request):
    export_translations()
    return redirect('db_locale_language_list')
