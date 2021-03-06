# Generated by Django 3.1.5 on 2021-01-12 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canChannel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=30)),
                ('comments', models.TextField(blank=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=20)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='cantrace.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=6, max_digits=10)),
                ('data_length', models.IntegerField()),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='cantrace.message')),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byte_id', models.IntegerField()),
                ('hex_data', models.CharField(max_length=2)),
                ('dec_data', models.IntegerField()),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cantrace.frame')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='trace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='channels', to='cantrace.trace'),
        ),
    ]
