# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubmittedLink'
        db.create_table(u'search_submittedlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('third_party_url', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'search', ['SubmittedLink'])


    def backwards(self, orm):
        # Deleting model 'SubmittedLink'
        db.delete_table(u'search_submittedlink')


    models = {
        u'search.scholarship': {
            'Meta': {'object_name': 'Scholarship'},
            'additional_restriction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'amount_usd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deadline2': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deadline3': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'deadline_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'essay_length_words': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'essay_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ethnicity_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gender_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gpa_restriction': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'graduate_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'high_school_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_restriction': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'min_age_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state_restriction': ('django_localflavor_us.models.USStateField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'street_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'third_party_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'undergrad_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'university_restriction': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.University']", 'null': 'True', 'blank': 'True'})
        },
        u'search.submittedlink': {
            'Meta': {'object_name': 'SubmittedLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'third_party_url': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        u'search.university': {
            'Meta': {'object_name': 'University'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'homepage_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'profit_status': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'state': ('django_localflavor_us.models.USStateField', [], {'max_length': '2'}),
            'student_population': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'undergrad_tuition_nonresident': ('django.db.models.fields.IntegerField', [], {}),
            'undergrad_tuition_resident': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['search']