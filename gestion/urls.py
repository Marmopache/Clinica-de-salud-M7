from django.urls import path
from . import views

urlpatterns = [
    # Panel de control
    path('panel/', views.panel_control, name='panel_control'),
    # =========================
    # PACIENTES
    # =========================
    path('', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),
    path('pacientes/editar/<int:pk>/', views.PacienteUpdateView.as_view(), name='paciente_update'),
    path('pacientes/eliminar/<int:pk>/', views.PacienteDeleteView.as_view(), name='paciente_delete'),

    # =========================
    # DOCTORES
    # =========================
    path('doctores/', views.DoctorListView.as_view(), name='doctor_list'),
    path('doctores/nuevo/', views.DoctorCreateView.as_view(), name='doctor_create'),
    path('doctores/editar/<int:pk>/', views.DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctores/eliminar/<int:pk>/', views.DoctorDeleteView.as_view(), name='doctor_delete'),

    # =========================
    # HORAS MÉDICAS
    # =========================
    path('horas/', views.HoraMedicaListView.as_view(), name='hora_list'),
    path('horas/nuevo/', views.HoraMedicaCreateView.as_view(), name='hora_create'),
    path('horas/editar/<int:pk>/', views.HoraMedicaUpdateView.as_view(), name='hora_update'),
    path('horas/eliminar/<int:pk>/', views.HoraMedicaDeleteView.as_view(), name='hora_delete'),
]



