from django.test import TestCase
from .models import Paciente, Doctor, HoraMedica
from datetime import date, time

# --------------------
# TESTS DOCTOR
# --------------------
class DoctorTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            nombre="Juan",
            apellido_paterno="Perez",
            apellido_materno="Gomez",
            fecha_nacimiento=date(1980,5,10),
            especialidad="Cardiología"
        )

    def test_crear_doctor(self):
        """Verifica que el doctor se crea correctamente"""
        self.assertEqual(self.doctor.nombre, "Juan")

    def test_actualizar_especialidad(self):
        """Verifica que se puede actualizar la especialidad"""
        self.doctor.especialidad = "Neurología"
        self.doctor.save()
        self.assertEqual(Doctor.objects.get(id=self.doctor.id).especialidad, "Neurología")

    def test_calcular_edad(self):
        """Verifica que la propiedad edad devuelve correctamente la edad"""
        edad_esperada = date.today().year - 1980
        if (date.today().month, date.today().day) < (5, 10):
            edad_esperada -= 1
        self.assertEqual(self.doctor.edad, edad_esperada)

# --------------------
# TESTS PACIENTE
# --------------------
class PacienteTest(TestCase):
    def setUp(self):
        self.paciente = Paciente.objects.create(
            nombre="Luis",
            apellido_paterno="Ramirez",
            apellido_materno="Lopez",
            fecha_nacimiento=date(2005,8,20)
        )

    def test_crear_paciente(self):
        """Verifica creación de paciente"""
        self.assertEqual(self.paciente.nombre, "Luis")

    def test_actualizar_paciente(self):
        """Verifica actualización de datos de paciente"""
        self.paciente.nombre = "Luis Alberto"
        self.paciente.save()
        self.assertEqual(Paciente.objects.get(id=self.paciente.id).nombre, "Luis Alberto")

    def test_calcular_edad(self):
        """Verifica que la edad se calcula correctamente"""
        edad_esperada = date.today().year - 2005
        if (date.today().month, date.today().day) < (8, 20):
            edad_esperada -= 1
        self.assertEqual(self.paciente.edad, edad_esperada)

# --------------------
# TESTS HORA MEDICA
# --------------------
class HoraMedicaTest(TestCase):
    def setUp(self):
        self.doctor = Doctor.objects.create(
            nombre="Ana",
            apellido_paterno="Lopez",
            apellido_materno="Diaz",
            fecha_nacimiento=date(1985,4,5),
            especialidad="Pediatría"
        )
        self.paciente = Paciente.objects.create(
            nombre="Sofia",
            apellido_paterno="Martinez",
            apellido_materno="Perez",
            fecha_nacimiento=date(2010,7,10)
        )
        self.hora = HoraMedica.objects.create(
            paciente=self.paciente,
            doctor=self.doctor,
            fecha=date.today(),
            hora=time(10,0),
            motivo="Chequeo general"
        )

    def test_crear_hora_medica(self):
        """Verifica que se crea correctamente una hora médica"""
        self.assertEqual(self.hora.paciente.nombre, "Sofia")

    def test_actualizar_motivo(self):
        """Verifica que se puede actualizar el motivo de la hora médica"""
        self.hora.motivo = "Vacunación"
        self.hora.save()
        self.assertEqual(HoraMedica.objects.get(id=self.hora.id).motivo, "Vacunación")

    def test_filtro_por_doctor(self):
        """Verifica que el filtro por doctor funciona"""
        horas = HoraMedica.objects.filter(doctor=self.doctor)
        self.assertEqual(horas.count(), 1)