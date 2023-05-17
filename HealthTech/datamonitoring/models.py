from django.db import models

class VitalSigns(models.Model):
    patient = models.ForeignKey('usermanagement.Patient', on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=20)
    heart_rate = models.IntegerField()
    respiratory_rate = models.IntegerField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    oxygen_saturation = models.IntegerField()
    pain_level = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vital Signs"

    def __str__(self):
        return f"{self.patient.username}'s Vital Signs at {self.timestamp}"
