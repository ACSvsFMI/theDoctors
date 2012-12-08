# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UsersAndActions'
        db.delete_table('trakc_usersandactions')

        # Deleting model 'ActionsAndPosts'
        db.delete_table('trakc_actionsandposts')

        # Adding field 'Post.likes'
        db.add_column('trakc_post', 'likes',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Post.shares'
        db.add_column('trakc_post', 'shares',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Post.comments'
        db.add_column('trakc_post', 'comments',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Action.name'
        db.delete_column('trakc_action', 'name')

        # Adding field 'Action.user'
        db.add_column('trakc_action', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Action.like_cost'
        db.add_column('trakc_action', 'like_cost',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Action.share_cost'
        db.add_column('trakc_action', 'share_cost',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Action.comment_cost'
        db.add_column('trakc_action', 'comment_cost',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'UsersAndActions'
        db.create_table('trakc_usersandactions', (
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Action'])),
            ('action_cost', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('trakc', ['UsersAndActions'])

        # Adding model 'ActionsAndPosts'
        db.create_table('trakc_actionsandposts', (
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Action'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trakc.Post'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('action_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('trakc', ['ActionsAndPosts'])

        # Deleting field 'Post.likes'
        db.delete_column('trakc_post', 'likes')

        # Deleting field 'Post.shares'
        db.delete_column('trakc_post', 'shares')

        # Deleting field 'Post.comments'
        db.delete_column('trakc_post', 'comments')


        # User chose to not deal with backwards NULL issues for 'Action.name'
        raise RuntimeError("Cannot reverse this migration. 'Action.name' and its values cannot be restored.")
        # Deleting field 'Action.user'
        db.delete_column('trakc_action', 'user_id')

        # Deleting field 'Action.like_cost'
        db.delete_column('trakc_action', 'like_cost')

        # Deleting field 'Action.share_cost'
        db.delete_column('trakc_action', 'share_cost')

        # Deleting field 'Action.comment_cost'
        db.delete_column('trakc_action', 'comment_cost')


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
            'comment_cost': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'like_cost': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'share_cost': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'trakc.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['trakc.Target']"}),
            'comments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('json_field.fields.JSONField', [], {'default': '{}'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'shares': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'trakc.target': {
            'Meta': {'object_name': 'Target'},
            'google_id': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'target_photo': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'targeted_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'targeted_by'", 'symmetrical': 'False', 'through': "orm['trakc.UsersAndTargets']", 'to': "orm['auth.User']"})
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