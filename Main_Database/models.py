from sqlite3 import PrepareProtocol
from unittest.util import _MAX_LENGTH
from django.db import models
from multiselectfield  import MultiSelectField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class PersonContact(models.Model):
    name=models.CharField('Name',max_length=100)
    designation=models.CharField('Designation',max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Organization(models.Model):
    ORGANIZATION_TYPE_CHOICES=(
        ('CBOs','CBOs'),
        ('CSOs','CSOs'),
        ('Hospitals','Hospitals'),
        ('NGOs','NGOs'),
        ('Women Groups','Women Groups'),
        ('Youth Groups','Youth Groups'),
        )
    name=models.CharField('name',max_length=100)
    organization_type=models.CharField('Organization Type',max_length=100,choices=ORGANIZATION_TYPE_CHOICES)
    focus=models.CharField('Focus',max_length=100)
    email=models.EmailField()
    contact=models.ForeignKey(PersonContact,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
# class Grants
THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G')    
    )

class Grant(models.Model):
    PERSON_RESPONSIBLE=(
        ('Timoty','Timothy'),
        ('Lisa','Lisa'),
        ('Tara','Tara'),
        ('Jesica','Jesica'),
        ('Mitchelle','Mitchelle'), 
        ('Nyokabi','Nyokabi'),
        ('Dorcas','Dorcas'),
        ('Ken','Ken'),
        ('Martha','Martha') ,            
    )
    FREQUENCY=(
        ('Annual','Annual'),
        ('Bi-annual','Bi-annual'),    
    )
    CURRENCY=(
        ('USD','USD'),
        ('Ksh','Ksh'),   
    )

    # thematic_area=MultiSelectField(choices=THEMATIC_CHOIECES)
    thematic_area=models.CharField('Choose Persons',choices=THEMATIC_CHOIECES,max_length=100)
    donor=models.CharField('Donor',max_length=200,blank=True,null=True)
    project_name=models.CharField('Project Name',max_length=200)
    # person_responsible=MultiSelectField(PERSON_RESPONSIBLE,max_choices=3,max_length=10)
    person_responsible=models.CharField('Choose Persons',choices=PERSON_RESPONSIBLE,max_length=100)

    # frequency=MultiSelectField(choices=FREQUENCY,max_choices=2,max_length=10)
    frequency=models.CharField('Choose Persons',choices=FREQUENCY,max_length=100)
    project_start=models.DateField()
    project_end=models.DateField()
    value=models.IntegerField()
    currency=models.CharField('Choose Currency',max_length=100,choices=CURRENCY)

    def __str__(self):
        return self.project_name
THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G'),     
    )
# activivity details
class ActivityDetail(models.Model):
    THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G'),     
    )
    ACTIVITY_TYPE_CHOICES=(
        ('Training','Training'),
        ('Meeting','Meeting'),
        ('Workshop','Workshop'),
        )

    COUNTY=(
        ('Nairobi','Nairobi'),
        ('Kisumu','Kisumu'),
        ('Kajiado','Kajiado'),
        ('Homabay','Homabay'),
        ('Machakos','Machakos'),
        ('Nakuru','Nakuru'),
        ('Siaya','Siaya'),
        )
    name=models.CharField('Activity name',max_length=100)
    activity_type=models.CharField('Activity Type',max_length=100,choices=ACTIVITY_TYPE_CHOICES)
    thematic=models.CharField('Choose Thematic',choices=THEMATIC_CHOIECES,max_length=100)
    project=models.ForeignKey(Grant,on_delete=models.CASCADE)
    venue=models.CharField('Choose venue',choices=COUNTY,max_length=100)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()

    def __str__(self):
        return self.name

# Participant
class AddParticipant(models.Model):
    activity_name=models.ForeignKey(ActivityDetail,on_delete=models.CASCADE)
    total_activity=models.IntegerField(default=50)

    

    def __str__(self):
        return str(self.activity_name)

class Participant(models.Model):
    COUNTY=(
        ('Nairobi','Nairobi'),
        ('Kisumu','Kisumu'),
        ('Kajiado','Kajiado'),
        ('Homabay','Homabay'),
        ('Machakos','Machakos'),
        ('Nakuru','Nakuru'),
        ('Siaya','Siaya'),
        )

    GENDER_CHOICES=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    TYPE_CHOICES=(
        ('Widows','Widows'),
        ('Elders','Elders'),
        ('Doctors','Doctors'),
        ('Nurses','Nurses'),
        ('Lawyers','Lawyers'),
        ('Adolescent Ladies','Adolesecnt Ladies'),
        ('Youths','Youths'),
        ('Judges','Judges'),     
    )
    activity=models.ForeignKey(AddParticipant, on_delete=models.CASCADE,)
    name=models.CharField('name',max_length=100)
    id_number=models.IntegerField('id number')
    phone=models.CharField('Phone',max_length=100)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE)
    gender=models.CharField('Gender',choices=GENDER_CHOICES,max_length=100)
    type=models.CharField('Choose Designation(type)',choices=TYPE_CHOICES,max_length=100)
    county=models.CharField('Choose County',choices=COUNTY,max_length=100)
    email=models.EmailField(blank=True,null=True)

    def __str__(self):
        return self.name 
# polls

THEMATIC_CHOIECES=(
        ('SRHR','SRHR'),
        ('HIV/TB','HIV/TB'),
        ('WLPR','WLPR'),
        ('SILU','SILU'),
        ('H&G','H&G')    
    )
ACTIVITY_CHOICES=(
        ('Activity X','Activity X'),
        ('Activity Y','Activity Y'),
        ('Activity Z','Activity Z'),
        ('Activity W','Activity W')
 )

class Poll(models.Model):
    thematic=models.CharField('Choose Thematic',choices=THEMATIC_CHOIECES,max_length=100 ,default='SRHR')
    activity=models.CharField('Choose Activity',choices=ACTIVITY_CHOICES,max_length=100,default='Activity X')
    question=models.TextField()
    option_one=models.CharField('Option One',max_length=100,blank=True,null=True)
    option_two=models.CharField('Option Two',max_length=100,blank=True,null=True)
    option_three=models.CharField('Option Three',max_length=100,blank=True,null=True)
    option_four=models.CharField('Option Four',max_length=100,blank=True,null=True)
    option_five=models.CharField('Option Five',max_length=100,blank=True,null=True)
    option_six=models.CharField('Option Six',max_length=100,blank=True,null=True)
    option_one_count=models.IntegerField(default=0)
    option_two_count=models.IntegerField(default=0)
    option_three_count=models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)
    option_five_count=models.IntegerField(default=0)
    option_six_count=models.IntegerField(default=0)

    def __str__(self):
        return self.question

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count + self.option_five_count + self.option_six_count


class Post(models.Model):
    title=models.CharField('Title',max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=RichTextField(blank=True, null=True)

    def __str__(self):

        return self.title + ' | '+str(self.author)
    




