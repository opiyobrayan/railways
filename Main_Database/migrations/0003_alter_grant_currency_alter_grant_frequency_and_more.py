# Generated by Django 4.1.1 on 2022-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_Database', '0002_rename_participint_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('Ksh', 'Ksh')], max_length=100, verbose_name='Choose Currency'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='frequency',
            field=models.CharField(choices=[('Annual', 'Annual'), ('Bi-annual', 'Bi-annual')], max_length=100, verbose_name='Choose Persons'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='person_responsible',
            field=models.CharField(choices=[('Timoty', 'Timothy'), ('Lisa', 'Lisa'), ('Tara', 'Tara'), ('Jesica', 'Jesica'), ('Mitchelle', 'Mitchelle'), ('Nyokabi', 'Nyokabi'), ('Dorcas', 'Dorcas'), ('Ken', 'Ken'), ('Martha', 'Martha')], max_length=100, verbose_name='Choose Persons'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='thematic_area',
            field=models.CharField(choices=[('SRHR', 'SRHR'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU'), ('H&G', 'H&G')], max_length=100, verbose_name='Choose Persons'),
        ),
    ]
