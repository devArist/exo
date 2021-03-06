# Generated by Django 3.2 on 2021-05-07 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_auto_20210507_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pointure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('valeur', models.IntegerField(blank=True, null=True, verbose_name='valeur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Taille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='nom')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='article',
            name='taille',
        ),
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('H', 'Hommes'), ('F', 'Femmes'), ('HF', 'All')], default='HF', max_length=50),
        ),
        migrations.AlterField(
            model_name='star',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='service.article', verbose_name='utlisateur'),
        ),
        migrations.AddField(
            model_name='article',
            name='pointure',
            field=models.ManyToManyField(related_name='article_pointure', to='service.Pointure'),
        ),
        migrations.AddField(
            model_name='article',
            name='taille',
            field=models.ManyToManyField(related_name='article_taille', to='service.Taille'),
        ),
    ]
