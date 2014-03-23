# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'demo2_author', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'demo2', ['Author'])

        # Adding model 'BookAuthors'
        db.create_table(u'demo2_bookauthors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo2.Author'])),
            ('book', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['demo2.Book'])),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal(u'demo2', ['BookAuthors'])

        # Adding model 'Book'
        db.create_table(u'demo2_book', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('abstract', self.gf('django.db.models.fields.TextField')()),
            ('price_net', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'demo2', ['Book'])


    def backwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'demo2_author')

        # Deleting model 'BookAuthors'
        db.delete_table(u'demo2_bookauthors')

        # Deleting model 'Book'
        db.delete_table(u'demo2_book')


    models = {
        u'demo2.author': {
            'Meta': {'ordering': "('last_name',)", 'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'demo2.book': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Book'},
            'abstract': ('django.db.models.fields.TextField', [], {}),
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['demo2.Author']", 'through': u"orm['demo2.BookAuthors']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_net': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'demo2.bookauthors': {
            'Meta': {'ordering': "('order',)", 'object_name': 'BookAuthors'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo2.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['demo2.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['demo2']