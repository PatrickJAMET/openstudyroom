# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-18 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import machina.core.validators
import machina.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, unique=True)),
                ('slug', models.CharField(blank=True, max_length=5, unique=True)),
                ('close', models.BooleanField(default=False)),
                ('private', models.BooleanField(default=False)),
                ('promote', models.BooleanField(default=False)),
                ('description', machina.models.fields.MarkupTextField(blank=True, no_rendered_field=True, null=True, validators=[machina.core.validators.NullableMaxLengthValidator(2000)])),
                ('private_description', machina.models.fields.MarkupTextField(blank=True, no_rendered_field=True, null=True, validators=[machina.core.validators.NullableMaxLengthValidator(2000)])),
                ('_description_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('_private_description_rendered', models.TextField(blank=True, editable=False, null=True)),
                ('admin_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_community', to='auth.Group')),
                ('user_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_community', to='auth.Group')),
            ],
        ),
    ]
