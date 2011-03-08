Django DB Locale
====================

Usage
-----

This application get the list of languages from settings.LANGUAGES and improve ability translating strings from database.
You can translate these strings in web `/db_locale/`.
After you finish translating use `Apply translation` link and than compile translations ( `./manage.py compilemessages` ).

Settings
--------

If you have the application `test_app` with the following model:

	class Book(models.Model):
        name = models.CharField(max_length=255)
        content = models.TextField()
        author = models.ForeignKey(User)
		
And you want translate `name`, `content` fields you can add these lines into settings.py:

    DB\_LOCALE\_TRANSLATE\_ITEMS = (
        ('test_app.models.Book', ('name', 'content')),
    )

Installation
------------

1. Add "db\_locale" to your INSTALLED\_APPS
2. Migrate database
3. Bind the `db_locale` urls.py into your main urls.py with something like: `url(r'^db_locale/', include('db_locale.urls')),`
4. Configure settings
5. Import existing django.po files. ( `./manage.py import_translations_from_po` )
6. Profit
