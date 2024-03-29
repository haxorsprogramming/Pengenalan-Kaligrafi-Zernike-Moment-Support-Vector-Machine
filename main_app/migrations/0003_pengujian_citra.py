# Generated by Django 3.1.4 on 2021-02-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_nilai_data_latih'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengujian_Citra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kd_uji', models.CharField(max_length=50)),
                ('nama_pengujian', models.CharField(max_length=150)),
                ('waktu_pengujian', models.DateTimeField()),
                ('base_svm_final', models.FloatField()),
                ('hasil_final', models.CharField(max_length=150)),
            ],
        ),
    ]
