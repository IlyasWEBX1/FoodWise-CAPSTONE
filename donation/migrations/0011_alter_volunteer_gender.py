# Generated by Django 5.2 on 2025-06-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0010_donationtransaction_delivery_evidence_fooditem_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='gender',
            field=models.CharField(choices=[('Male', 'Laki-laki'), ('Female', 'Perempuan')], default='Male', max_length=10),
            preserve_default=False,
        ),
    ]
