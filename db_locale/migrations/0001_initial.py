# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Translation'
        db.create_table('db_locale_translation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('msgid', self.gf('django.db.models.fields.TextField')()),
            ('msgstr', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('db_locale', ['Translation'])


    def backwards(self, orm):
        
        # Deleting model 'Translation'
        db.delete_table('db_locale_translation')


    models = {
        'db_locale.translation': {
            'Meta': {'object_name': 'Translation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'msgid': ('django.db.models.fields.TextField', [], {}),
            'msgstr': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['db_locale']
