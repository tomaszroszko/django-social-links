# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SocialLinkType'
        db.create_table(u'sociallinks_sociallinktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('css_class', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'sociallinks', ['SocialLinkType'])

        # Adding model 'SocialLinkGroup'
        db.create_table(u'sociallinks_sociallinkgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'sociallinks', ['SocialLinkGroup'])

        # Adding model 'SocialLink'
        db.create_table(u'sociallinks_sociallink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sociallinks.SocialLinkType'])),
            ('link_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sociallinks.SocialLinkGroup'], null=True, blank=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True)),
            ('object_pk', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('priority', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'sociallinks', ['SocialLink'])


    def backwards(self, orm):
        # Deleting model 'SocialLinkType'
        db.delete_table(u'sociallinks_sociallinktype')

        # Deleting model 'SocialLinkGroup'
        db.delete_table(u'sociallinks_sociallinkgroup')

        # Deleting model 'SocialLink'
        db.delete_table(u'sociallinks_sociallink')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'sociallinks.sociallink': {
            'Meta': {'ordering': "('priority',)", 'object_name': 'SocialLink'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sociallinks.SocialLinkGroup']", 'null': 'True', 'blank': 'True'}),
            'link_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sociallinks.SocialLinkType']"}),
            'object_pk': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'priority': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        },
        u'sociallinks.sociallinkgroup': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SocialLinkGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'sociallinks.sociallinktype': {
            'Meta': {'ordering': "('name',)", 'object_name': 'SocialLinkType'},
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['sociallinks']