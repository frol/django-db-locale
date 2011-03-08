#!/usr/bin/env python

import os
from lockfile import FileLock

from db_locale import settings
from django.core.management.base import BaseCommand

from db_locale.utils import import_translations_from_po

LOCK_FILE = 'import_translations_from_po'
video_filters = ['*.*']

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Check whether it is already running or not
        lock = FileLock(os.path.join(settings.LOCK_ROOT, LOCK_FILE))
        try:
            lock.acquire(0)
        except:
            print ("It seems the command is processing already.")
            return

        import_translations_from_po()
        lock.release()
