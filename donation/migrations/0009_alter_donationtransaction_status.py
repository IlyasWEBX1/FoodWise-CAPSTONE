# Generated by Django 5.2 on 2025-05-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0008_alter_donationtransaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationtransaction',
            name='status',
            field=models.CharField(choices=[('Menunggu Diambil', 'Menunggu Diambil'), ('Menunggu Disalurkan', 'Menunggu Disalurkan'), ('Telah Disalurkan', 'Telah Disalurkan'), ('Selesai', 'Selesai')], default='Menunggu Diambil', max_length=50),
        ),
    ]
