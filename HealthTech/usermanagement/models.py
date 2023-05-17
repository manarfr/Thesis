from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.

class CustomUser(AbstractUser):
    pass

class Patient(CustomUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    age = models.PositiveIntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    medical_history = models.TextField(blank=True)
    current_condition = models.TextField(blank=True)
    admission_date = models.DateField(blank=True, null=True)
    discharge_date = models.DateField(blank=True, null=True)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    patient_groups = models.ManyToManyField(Group, related_name='patient_users')


class Doctor(CustomUser):
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    speciality = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name)
    doctors_groups = models.ManyToManyField(Group, related_name='doctor_users')

