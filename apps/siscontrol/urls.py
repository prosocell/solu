# -*- coding: utf-8 -*-
from __future__ import unicode_literals,absolute_import
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from .views import(
    SignUpview, 
    siscontrol, 
    infdoc, 
    Comunicado_list, 
    directivo, 
    calificaciones,
    horario, 
    edit_comunicado, 
    controlsystem, 
    list_com, 
    delete_comu, 
    subircomunicado, 
    change_password, 
    forma,
    pag,
    convo,
    nuevo,
    cursador,
    normal,
    repite,
    subirextra,
    admin_extra,
    delete_extra,
    user_list_dir,
    user_list_doc,
    user_list_alum,
    user_list_aluv,
    user_list_para,
    delete_user,
    cal_par,
    list_horarios,
    edit_user,
    delete_horario,
    subircalificacion
    ) 

urlpatterns = [
    path('',LoginView.as_view(template_name='siscontrol/index.html'), name='index'),
    path('siscontrol/', include('django.contrib.auth.urls')),
    path('control', controlsystem, name="control"),
    path('user_list_dir/', user_list_dir.as_view(), name="user_list_dir"),
    path('user_list_doc/', user_list_doc.as_view(), name="user_list_doc"),
    path('user_list_alum/', user_list_alum.as_view(), name="user_list_alum"),
    path('user_list_aluv/', user_list_aluv.as_view(), name="user_list_aluv"),
    path('user_list_para/', user_list_para.as_view(), name="user_list_para"),
    path('delete_user/<int:pk>/', delete_user.as_view(),name="delete_user"),
    path('edit_user/<int:pk>/', edit_user.as_view(), name="edit_user"),
	#Registro
	path('signup/', SignUpview.as_view(), name ="signup"),
    path('camb_password', change_password, name="camb_password" ),
	path('login/', LoginView.as_view(), name="login"),
	#Docentes#alumnos#Informacion
	path('infdoc/<int:pk>/', infdoc.as_view(), name="infdoc"),
	#Directivo
	path('directivo/', directivo, name="directivo" ),  
    #comunicados
    path('comunicadosgeneral/', Comunicado_list.as_view(), name="comunicadosgeneral"), 
    path('list-comunicado/', list_com.as_view(), name="list-comunicado"),
    path('delete_comu/<int:pk>', delete_comu.as_view(), name="delete_comu"),
    path('edit-comu/<int:pk>/', edit_comunicado.as_view(), name="edit-comu"),
    path('subircomunicado/', subircomunicado, name="subircomunicado"),
    ########Admin#######
    #calificaciones
    path('calificaciones/', calificaciones.as_view(), name="calificaciones"),
    path('cal_par/', cal_par.as_view(), name="cal_par"),
    path('subircal', subircalificacion.as_view(), name="subircal"),
    #horarios
    path('horario/', horario.as_view(), name="horario"),
    path('list_horarios', list_horarios.as_view(), name="list_horarios"),
    path('delete_horario/', delete_horario, name="delete_horario"),
    #extraescolar#
    path('subirextra/', subirextra, name="subirextra"),
    path('admin_extra', admin_extra.as_view(), name="admin_extra"),
    path('delete_extra/<int:pk>', delete_extra.as_view(), name="delete_extra"),
    #PDF´S#
    path('formato/', forma, name="formato"),
    path('pago/', pag, name="pago"),
    path('convocatoria/', convo, name="convocatoria"),
    path('nuevo/', nuevo, name='nuevo'),
    path('cursador/', cursador, name='cursadores'),
    path('normal/', normal, name='normal'),
    path('repetidor', repite, name='repetidor'),
]	