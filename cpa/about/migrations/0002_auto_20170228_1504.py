# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-28 15:04
from __future__ import unicode_literals

import core.blocks
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'intro', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'alignment', core.blocks.ImageFormatChoiceBlock())], icon='image', label='Aligned image'))]),
        ),
    ]