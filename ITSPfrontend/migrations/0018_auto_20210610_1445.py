# Generated by Django 3.2.2 on 2021-06-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ITSPfrontend', '0017_auto_20210610_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='member1email',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member1name',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member1phoneno',
            field=models.CharField(blank=True, default='enter', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2email',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2name',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member2phoneno',
            field=models.CharField(blank=True, default='enter', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3email',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3name',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='member3phoneno',
            field=models.CharField(blank=True, default='enter', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='teamid',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='teamleaderemail',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='teamleadername',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='teamleaderphoneno',
            field=models.CharField(blank=True, default='enter', max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='info',
            name='teamname',
            field=models.CharField(blank=True, default='enter', max_length=122, null=True),
        ),
    ]
