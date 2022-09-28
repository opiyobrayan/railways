# Generated by Django 4.1.1 on 2022-09-25 05:29

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Activity name')),
                ('activity_type', models.CharField(choices=[('Training', 'Training'), ('Meeting', 'Meeting'), ('Workshop', 'Workshop')], max_length=100, verbose_name='Activity Type')),
                ('thematic', models.CharField(choices=[('SRHR', 'SRHR'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU'), ('H&G', 'H&G')], max_length=100, verbose_name='Choose Thematic')),
                ('venue', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Kajiado', 'Kajiado'), ('Homabay', 'Homabay'), ('Machakos', 'Machakos'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya')], max_length=100, verbose_name='Choose venue')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic_area', multiselectfield.db.fields.MultiSelectField(choices=[('SRHR', 'SRHR'), ('HIV/TB', 'HIV/TB'), ('WLPR', 'WLPR'), ('SILU', 'SILU'), ('H&G', 'H&G')], max_length=100)),
                ('donor', models.CharField(blank=True, max_length=200, null=True, verbose_name='Donor')),
                ('project_name', models.CharField(max_length=200, verbose_name='Project Name')),
                ('person_responsible', multiselectfield.db.fields.MultiSelectField(max_length=100, verbose_name=(('Timoty', 'Timothy'), ('Lisa', 'Lisa'), ('Tara', 'Tara'), ('Jesica', 'Jesica'), ('Mitchelle', 'Mitchelle'), ('Nyokabi', 'Nyokabi'), ('Dorcas', 'Dorcas'), ('Ken', 'Ken'), ('Martha', 'Martha')))),
                ('frequency', multiselectfield.db.fields.MultiSelectField(choices=[('Annual', 'Annual'), ('Bi-annual', 'Bi-annual')], max_length=100)),
                ('project_start', models.DateField()),
                ('project_end', models.DateField()),
                ('value', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('Ksh', 'Ksh')], max_length=100, verbose_name='Chooce Currency')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('organization_type', models.CharField(choices=[('CBOs', 'CBOs'), ('CSOs', 'CSOs'), ('Hospitals', 'Hospitals'), ('NGOs', 'NGOs'), ('Women Groups', 'Women Groups'), ('Youth Groups', 'Youth Groups')], max_length=100, verbose_name='Organization Type')),
                ('focus', models.CharField(max_length=100, verbose_name='Focus')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PersonContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('designation', models.CharField(max_length=100, verbose_name='Designation')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Participint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('id_number', models.IntegerField(verbose_name='id number')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=100, verbose_name='Gender')),
                ('type', models.CharField(choices=[('Widows', 'Widows'), ('Elders', 'Elders'), ('Doctors', 'Doctors'), ('Nurses', 'Nurses'), ('Lawyers', 'Lawyers'), ('Adolescent Ladies', 'Adolesecnt Ladies'), ('Youths', 'Youths'), ('Judges', 'Judges')], max_length=100, verbose_name='Choose Designation(type)')),
                ('county', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Kajiado', 'Kajiado'), ('Homabay', 'Homabay'), ('Machakos', 'Machakos'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya')], max_length=100, verbose_name='Choose County')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('activity', models.ForeignKey(limit_choices_to={'name': True}, on_delete=django.db.models.deletion.CASCADE, to='Main_Database.activitydetail')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_Database.organization')),
            ],
        ),
        migrations.AddField(
            model_name='organization',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_Database.personcontact'),
        ),
        migrations.AddField(
            model_name='activitydetail',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_Database.grant'),
        ),
    ]
