# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Book'
        db.create_table(u'demo1_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'demo1', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Book'
        db.delete_table(u'demo1_book')


    models = {
        u'demo1.book': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Book'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['demo1']