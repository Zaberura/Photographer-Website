# Generated by Django 4.2.2 on 2023-06-25 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_project_photosource_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photosource',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.project'),
        ),
    ]
