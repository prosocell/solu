# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path,include
from django.contrib.auth.views import LoginView,LogoutView
from apps.inicio.views import (
	contact,
	quinsom,
	prop,
	orga,
	mivi,
	valo,
	equidir,
	calen,
    forma,
    norm,
    nuev,
    pag,
    repe,
    cursa,
    convo,
	comu_extra_basquet,
 	comu_extra_futbol,
    comu_extra_taekwondo,
    comu_extra_hawaiano,
    comu_extra_danza,
    comu_extra_marimba,
    comu_extra_voca,
    comu_extra_bandaguerra,
    comu_extra_tochito,
    comu_extra_escolta,
    comu_extra_voli,
    comu_extra_dibujo
    )

urlpatterns = [
    path('',LoginView.as_view(template_name='index.html'), name='index'),
    path('contact/',contact, name="contact"), 
    path('quinsom/', quinsom, name="quinsom"),
    path('proposito/', prop, name="proposito"),
    path('organigrama/',orga, name="organigrama"),
    path('mivi/', mivi, name="mivi"),
    path('valores/', valo, name="valores"),
    path('equidir/', equidir, name="equidir"),
    path('calendario/', calen, name="calendario"),
    path('alumno_cursador_normal/', norm, name="alumno_cursador_normal"),
    path('formatos_de_inscripcion/', forma, name="formatos_de_inscripcion"),
    path('pago_inscripcion/', pag, name="pago_inscripcion"),
    path('alumno_repetidor/', repe, name="alumno_repetidor"),
    path('alumno_cursador/', cursa, name="alumno_cursador"),
    path('convocatoria/', convo, name="convocatoria"),
    path('comu_extra_basquet/', comu_extra_basquet.as_view(), name="comu_extra_basquet"),
    path('comu_extra_futbol/', comu_extra_futbol.as_view(), name="comu_extra_futbol"),
    path('comu_extra_taekwondo/', comu_extra_taekwondo.as_view(), name="comu_extra_taekwondo"),
    path('comu_extra_hawaiano/', comu_extra_hawaiano.as_view(), name="comu_extra_hawaiano"),
    path('comu_extra_danza/', comu_extra_danza.as_view(), name="comu_extra_danza"),
    path('comu_extra_marimba/', comu_extra_marimba.as_view(), name="comu_extra_marimba"),
    path('comu_extra_voca/', comu_extra_voca.as_view(), name="comu_extra_voca"),
    path('comu_extra_bandaguerra/', comu_extra_bandaguerra.as_view(), name="comu_extra_bandaguerra"),
    path('comu_extra_tochito/', comu_extra_tochito.as_view(), name="comu_extra_tochito"),
    path('comu_extra_escolta/', comu_extra_escolta.as_view(), name="comu_extra_escolta"),
    path('comu_extra_voli/', comu_extra_voli.as_view(), name="comu_extra_voli"),
    path('comu_extra_dibujo/', comu_extra_dibujo.as_view(), name="comu_extra_dibujo"),
    
]
