from django import forms
from .models import Paciente, Doctor, HoraMedica


# =========================
# PACIENTE
# =========================
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
        }


# =========================
# DOCTOR
# =========================
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'especialidad']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
        }


# =========================
# HORA MÉDICA
# =========================
class HoraMedicaForm(forms.ModelForm):
    class Meta:
        model = HoraMedica
        fields = ['paciente', 'doctor', 'fecha', 'hora', 'motivo']

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'motivo': forms.TextInput(attrs={'class': 'form-control'}),
        }