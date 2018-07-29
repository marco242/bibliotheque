# Generated by Django 2.0.5 on 2018-07-29 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(help_text='Ce champ nomme une categorie de manière unique', max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(help_text='Ce champ nomme une categorie de manière unique', max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.FileField(upload_to='Document')),
                ('fichier', models.FileField(upload_to='Document')),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(help_text='Ce champ nomme un domaie de manière unique', max_length=255, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eces.Domaine'),
        ),
        migrations.AddField(
            model_name='categorie',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eces.Domaine'),
        ),
    ]
