# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Scholarship.deadline2'
        db.add_column(u'search_scholarship', 'deadline2',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scholarship.deadline3'
        db.add_column(u'search_scholarship', 'deadline3',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Scholarship.deadline_type'
        db.add_column(u'search_scholarship', 'deadline_type',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Scholarship.high_school_eligible'
        db.add_column(u'search_scholarship', 'high_school_eligible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Scholarship.undergrad_eligible'
        db.add_column(u'search_scholarship', 'undergrad_eligible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'Scholarship.graduate_eligible'
        db.add_column(u'search_scholarship', 'graduate_eligible',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Scholarship.deadline'
        db.alter_column(u'search_scholarship', 'deadline', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Scholarship.deadline2'
        db.delete_column(u'search_scholarship', 'deadline2')

        # Deleting field 'Scholarship.deadline3'
        db.delete_column(u'search_scholarship', 'deadline3')

        # Deleting field 'Scholarship.deadline_type'
        db.delete_column(u'search_scholarship', 'deadline_type')

        # Deleting field 'Scholarship.high_school_eligible'
        db.delete_column(u'search_scholarship', 'high_school_eligible')

        # Deleting field 'Scholarship.undergrad_eligible'
        db.delete_column(u'search_scholarship', 'undergrad_eligible')

        # Deleting field 'Scholarship.graduate_eligible'
        db.delete_column(u'search_scholarship', 'graduate_eligible')


        # User chose to not deal with backwards NULL issues for 'Scholarship.deadline'
        raise RuntimeError("Cannot reverse this migration. 'Scholarship.deadline' and its values cannot be restored.")

    models = {
        u'search.scholarship': {
            'Meta': {'object_name': 'Scholarship'},
            'additional_restriction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'amount_usd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {}),
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
            'third_party_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'undergrad_eligible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'university_restriction': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['search.University']", 'null': 'True', 'blank': 'True'})
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