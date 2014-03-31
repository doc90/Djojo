# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ninja'
        db.create_table(u'dojo_ninja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('parentspermission', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('cellphone', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parentscellphone', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dojo', ['Ninja'])

        # Adding model 'Event'
        db.create_table(u'dojo_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateField')()),
            ('partecipantsnumber', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'dojo', ['Event'])

        # Adding M2M table for field partecipants on 'Event'
        m2m_table_name = db.shorten_name(u'dojo_event_partecipants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'dojo.event'], null=False)),
            ('ninja', models.ForeignKey(orm[u'dojo.ninja'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'ninja_id'])


    def backwards(self, orm):
        # Deleting model 'Ninja'
        db.delete_table(u'dojo_ninja')

        # Deleting model 'Event'
        db.delete_table(u'dojo_event')

        # Removing M2M table for field partecipants on 'Event'
        db.delete_table(db.shorten_name(u'dojo_event_partecipants'))


    models = {
        u'dojo.event': {
            'Meta': {'object_name': 'Event'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'partecipants': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['dojo.Ninja']", 'symmetrical': 'False', 'blank': 'True'}),
            'partecipantsnumber': ('django.db.models.fields.IntegerField', [], {}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'dojo.ninja': {
            'Meta': {'object_name': 'Ninja'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'cellphone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parentscellphone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'parentspermission': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['dojo']