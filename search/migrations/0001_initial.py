# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'University'
        db.create_table(u'search_university', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('homepage_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django_localflavor_us.models.USStateField')(max_length=2)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('student_population', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('undergrad_tuition_resident', self.gf('django.db.models.fields.IntegerField')()),
            ('undergrad_tuition_nonresident', self.gf('django.db.models.fields.IntegerField')()),
            ('profit_status', self.gf('django.db.models.fields.SmallIntegerField')(null=True)),
        ))
        db.send_create_signal(u'search', ['University'])

        # Adding model 'Scholarship'
        db.create_table(u'search_scholarship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('third_party_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateField')()),
            ('deadline', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('essay_required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('amount_usd', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('organization', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('min_age_restriction', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('state_restriction', self.gf('django_localflavor_us.models.USStateField')(max_length=2, blank=True)),
            ('essay_length_words', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gpa_restriction', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('additional_restriction', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('major_restriction', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('ethnicity_restriction', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('gender_restriction', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('sponsored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('status', self.gf('django.db.models.fields.SmallIntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'search', ['Scholarship'])

        # Adding M2M table for field university_restriction on 'Scholarship'
        m2m_table_name = db.shorten_name(u'search_scholarship_university_restriction')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('scholarship', models.ForeignKey(orm[u'search.scholarship'], null=False)),
            ('university', models.ForeignKey(orm[u'search.university'], null=False))
        ))
        db.create_unique(m2m_table_name, ['scholarship_id', 'university_id'])


    def backwards(self, orm):
        # Deleting model 'University'
        db.delete_table(u'search_university')

        # Deleting model 'Scholarship'
        db.delete_table(u'search_scholarship')

        # Removing M2M table for field university_restriction on 'Scholarship'
        db.delete_table(db.shorten_name(u'search_scholarship_university_restriction'))


    models = {
        u'search.scholarship': {
            'Meta': {'object_name': 'Scholarship'},
            'additional_restriction': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'amount_usd': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {}),
            'deadline': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'essay_length_words': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'essay_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ethnicity_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gender_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gpa_restriction': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_restriction': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'min_age_restriction': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sponsored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state_restriction': ('django_localflavor_us.models.USStateField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'third_party_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
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