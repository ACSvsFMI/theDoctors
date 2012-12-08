# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # Adding model 'Target'
        db.create_table('trakc_target', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('google_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('target_photo', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('trakc', ['Target'])

        # Adding model 'UsersAndTargets'
        db.create_table('trakc_usersandtargets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Target'])),
            ('platform', self.gf('json_field.fields.JSONField')(default={})),
        ))
        db.send_create_signal('trakc', ['UsersAndTargets'])

        # Adding model 'Post'
        db.create_table('trakc_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Target'])),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('trakc', ['Post'])

        # Adding model 'ActionsAndPosts'
        db.create_table('trakc_actionsandposts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Action'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Post'])),
            ('action_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('trakc', ['ActionsAndPosts'])

        # Adding model 'Action'
        db.create_table('trakc_action', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal('trakc', ['Action'])

        # Adding model 'UsersAndActions'
        db.create_table('trakc_usersandactions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Action'])),
            ('action_cost', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('trakc', ['UsersAndActions'])


    def backwards(self, orm):
        # Deleting model 'Target'
        db.delete_table('trakc_target')

        # Deleting model 'UsersAndTargets'
        db.delete_table('trakc_usersandtargets')

        # Deleting model 'Post'
        db.delete_table('trakc_post')

        # Deleting model 'ActionsAndPosts'
        db.delete_table('trakc_actionsandposts')

        # Deleting model 'Action'
        db.delete_table('trakc_action')

        # Deleting model 'UsersAndActions'
        db.delete_table('trakc_usersandactions')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'trakc.action': {
            'Meta': {'object_name': 'Action'},
            'cost': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'through': "orm['trakc.UsersAndActions']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        'trakc.actionsandposts': {
            'Meta': {'object_name': 'ActionsAndPosts'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Action']"}),
            'action_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Post']"})
        },
        'trakc.post': {
            'Meta': {'object_name': 'Post'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['trakc.Action']", 'through': "orm['trakc.ActionsAndPosts']", 'symmetrical': 'False'}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Target']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'trakc.target': {
            'Meta': {'object_name': 'Target'},
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'google_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'target_photo': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'targeted_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'targeted_by'", 'symmetrical': 'False', 'through': "orm['trakc.UsersAndTargets']", 'to': "orm['auth.User']"})
        },
        'trakc.usersandactions': {
            'Meta': {'object_name': 'UsersAndActions'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Action']"}),
            'action_cost': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'trakc.usersandtargets': {
            'Meta': {'object_name': 'UsersAndTargets'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform': ('json_field.fields.JSONField', [], {'default': '{}'}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Target']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['trakc']
