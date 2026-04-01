from django.contrib import admin
from .models import Paciente, Doctor, HoraMedica


# --------------------
# PACIENTES
# --------------------
@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'mostrar_edad')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno')
    list_filter = ('fecha_nacimiento',)

    def mostrar_edad(self, obj):
        return obj.calcular_edad()
    
    mostrar_edad.short_description = 'Edad'


# --------------------
# DOCTORES
# --------------------
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'especialidad', 'mostrar_edad')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'especialidad')
    list_filter = ('especialidad',)

    def mostrar_edad(self, obj):
        return obj.calcular_edad()
    
    mostrar_edad.short_description = 'Edad'


# --------------------
# HORAS MÉDICAS
# --------------------
@admin.register(HoraMedica)
class HoraMedicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'doctor', 'fecha', 'hora', 'motivo')
    search_fields = ('paciente__nombre', 'paciente__apellido_paterno', 'paciente__apellido_materno',
                     'doctor__nombre', 'doctor__apellido_paterno', 'doctor__apellido_materno', 'motivo')
    list_filter = ('fecha', 'doctor')