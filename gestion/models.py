from django.db import models
from datetime import date

# --------------------
# PACIENTES
# --------------------
class Paciente(models.Model):
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido_paterno = models.CharField(max_length=50, blank=False, null=False)
    apellido_materno = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad
    edad = property(calcular_edad) 
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"
# --------------------
# DOCTORES
# --------------------
class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50, blank=False, null=False)
    apellido_materno = models.CharField(max_length=50, blank=False, null=False)
    fecha_nacimiento = models.DateField()
    def calcular_edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad
    edad = property(calcular_edad) 
    especialidad = models.CharField(max_length=50) 
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"   
# --------------------
# HORAS MÉDICAS
# --------------------
class HoraMedica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} con {self.doctor}"
