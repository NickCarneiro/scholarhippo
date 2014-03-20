# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TimeStampedModel'
        db.create_table(u'report_timestampedmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['TimeStampedModel'])

        # Adding model 'Report'
        db.create_table(u'report_report', (
            (u'timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['report.TimeStampedModel'], unique=True, primary_key=True)),
            ('problem', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('explanation', self.gf('django.db.models.fields.TextField')()),
            ('ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
        ))
        db.send_create_signal(u'report', ['Report'])


    def backwards(self, orm):
        # Deleting model 'TimeStampedModel'
        db.delete_table(u'report_timestampedmodel')

        # Deleting model 'Report'
        db.delete_table(u'report_report')


    models = {
        u'report.report': {
            'Meta': {'object_name': 'Report', '_ormbases': [u'report.TimeStampedModel']},
            'explanation': ('django.db.models.fields.TextField', [], {}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'problem': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['report.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'report.timestampedmodel': {
            'Meta': {'object_name': 'TimeStampedModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['report']