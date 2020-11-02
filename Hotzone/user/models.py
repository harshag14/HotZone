from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=80, default="")
    idnumber = models.CharField(max_length=20)
    dateofbirth = models.DateField()

    def __str__(self):
        return f'{self.id}  {self.name}'

class Virus(models.Model):
    name = models.CharField(max_length=30)
    commonname = models.CharField(max_length=50)
    maxinfectiousperiod = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Viruses'

class Case(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    dateconfirmed = models.DateField()
    casetype = models.CharField(max_length=8)
    case_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.patient.name} {self.virus.name}'


class Location(models.Model):
    place = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    xcoord = models.FloatField()
    ycoord = models.FloatField()

    def __str__(self):
        return self.place


class CaseLocation(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    datefrom = models.DateField()
    dateto = models.DateField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return f' {self.case.case_id} {self.location.place}'

