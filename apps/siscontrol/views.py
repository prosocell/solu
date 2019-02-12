from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import UserCreationFormWithEmail, Comunicadosform, UploadFileForm, ComunicadoExtraform, user_subir, calificacionesform
from .models import User, comunicados_global, calificacion, horarios, comunicadoescolar
from django.db import models
from django.views.generic import CreateView
from django import forms
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from django.http import HttpResponse
import json
from pyexcel_xls import get_data
import pyexcel as pe




# Create your views here.
#index login
class user_list_dir(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        usuarios = User.objects.filter(turno="Di")
        return render(request,"siscontrol/user.html", {'usuarios':usuarios})

class user_list_doc(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        usuarios = User.objects.filter(turno="Mi")
        return render(request,"siscontrol/user.html", {'usuarios':usuarios})

class user_list_alum(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        usuarios = User.objects.filter(turno="Ma")
        return render(request,"siscontrol/user.html", {'usuarios':usuarios})

class user_list_aluv(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        usuarios = User.objects.filter(turno="Ve")
        return render(request,"siscontrol/user.html", {'usuarios':usuarios})

class user_list_para(ListView):
    model = User

    def get(self,request,*args,**kwargs):
        usuarios = User.objects.filter(turno="Pa")
        return render(request,"siscontrol/user.html", {'usuarios':usuarios})

class delete_user(DeleteView):
    model= User
    success_url = reverse_lazy('user_list')

class edit_user(UpdateView):
   model = User
   fields = ["first_name", "last_name","username", "email", "sexo", "nombreplan", "claveestado", "clacentro", "clavemuni", "clavelocal", "curp", "telefono", "turno", "orden", "rfc", "titulo"]
   template_name_suffix = '_update_form'

   def get_success_url(self):
    return reverse_lazy('edit_user', args=[self.object.id])

def controlsystem(request):
    return render(request,"siscontrol/index.html")  


def change_password(request):
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
    
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('camb_password')
            else:
                return redirect('camb_password')
        else:
            form = PasswordChangeForm(user=request.user)
            return render(request, "registration/change_password.html")

#vista de registro
class SignUpview(CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('signup')
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('signup') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpview, self).get_form()
        #modificar en tiempo real
        return form

    def subirinf(request):
        if request.method == 'POST':
            form = user_subir(request.POST)
            if form.is_valid():
                newuser = User(first_name = request.POST['first_name'],last_name= request.POST['last_name'], password1 = request.POST['password1'], password2 = request.POST[password2], email = request.POST['email'], nombreplan = request.POST['nombreplan'], claveestado = request.POST['claveestado'], clacentro = request.POST['clacentro'], clavemuni = request.POST['clavemuni'], clavelocal = request.POST['clavelocal'], curp = request.POST['curp'], telefono = request.POST['telefono'], orden = request.POST['orden'], rfc = request.POST['rfc'], titulo = request.POST['titulo'])
                newuser.save(form)
            else:
                form = user_subir()
        return render(request,'directivo/signupcom.html', {'form': form})


#vista index
def siscontrol(request):
	return render(request, "siscontrol/index.html")


#Docentes
class infdoc(TemplateView):
    model = User

    def get(self,request,*args,**kwargs):
        projects = User.objects.get(pk=self.kwargs['pk'])
        print(projects)
        return render(request, "docentes/infdoc.html", {'projects':projects})



class calificaciones(ListView):
    model = calificacion

    def get(self,request,*args, **kwargs):
        obj = request.user.matricula
        cal = calificacion.objects.filter(matricula=obj)
        return render (request, "calificaciones/calificaciones.html",{'cal':cal})

class cal_par(ListView):
    model = calificacion

    def get(self,request,*args,**kwargs):
        obj = request.user.grado
        obj1 = request.user.grupo
        cal = calificacion.objects.filter(semestre=obj,grupo=obj1)
        print(obj)
        print(obj1)
        return render(request, "calificaciones/cal_par.html", {'cal':cal})

#def subircalificacion(request):
 #   if request.method == 'POST':
  #      form = calificacionesform(request.POST)
   #     if form.is_valid():
    #        newdoc = calificacion(request.POST['clavemate'],request.POST['materia'],request.POST['semestre'],request.POST['grupo'],request.POST['clavegrupo'],request.POST['parcial_1'],request.POST['parcial_2'],request.POST['parcial_3'],request.POST['calificaci'],request.POST['prompar'],request.POST['promsem'],request.POST['inasistenc'],request.POST['numclases'], request.POST['inasispar1'],request.POST['inasispar2'],request.POST['inasispar3'],request.POST['matricula'],request.POST['rfc'])
     #       newdoc.save(form)
      #      return redirect("subircalificacion")
#    else:
       # form = calificacionesform()
  #  #tambien se puede utilizar render_to_response
 #   #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
#    return render(request, 'calificaciones/subircal.html', {'form': form})

class subircalificacion(CreateView):
    form_class = calificacionesform
    success_url = reverse_lazy('subircal')
    template_name = 'calificaciones/subircal.html'

    def get_success_url(self):
        return reverse_lazy('subircal') + '?register'

    def get_form(self, form_class=None):
        form = super(subircalificacion, self).get_form()
        #modificar en tiempo real
        return form

    def subirinf(request):
        if request.method == 'POST':
            form = calificacionesform(request.POST)
        if form.is_valid():
            newdoc = calificacion(request.POST['clavemate'],request.POST['materia'],request.POST['semestre'],request.POST['grupo'],request.POST['clavegrupo'],request.POST['parcial_1'],request.POST['parcial_2'],request.POST['parcial_3'],request.POST['calificaci'],request.POST['prompar'],request.POST['promsem'],request.POST['inasistenc'],request.POST['numclases'], request.POST['inasispar1'],request.POST['inasispar2'],request.POST['inasispar3'],request.POST['matricula'],request.POST['rfc'])
            newdoc.save(form)
            return redirect("subircalificacion")
        else:
            form = calificacionesform()
        return render(request, 'calificaciones/subircal.html', {'form': form})






# Directivo
def directivo(request):
    return render(request, "directivo/director.html")

##############################Comunicados############################
#Docente Alumno#
class Comunicado_list(ListView):
    model = comunicados_global
    
    def get(self,request,*args,**kwars):
        turno = request.user.turno
        #print(turno)
        comunicado = comunicados_global.objects.filter(turno=turno)
        #print(comunicado)
    
        return render(request, "comunicados_global_list/comunicados_global_list.html", {'comunicado':comunicado})

#subir  comunicado#Directivo#
#####opcion2#####
def subircomunicado(request):
    if request.method == 'POST':
        form = Comunicadosform(request.POST, request.FILES)
        if form.is_valid():
            newdoc = comunicados_global(title = request.POST['title'],description = request.POST['description'],turno = request.POST["turno"],archivo = request.FILES['archivo'])
            newdoc.save(form)
            return redirect("subircomunicado")
    else:
        form = Comunicadosform()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'directivo/signupcom.html', {'form': form})

#lista de comunicados#Directivo#
class list_com(ListView):
    model = comunicados_global

    def get(self,request,*args,**kwars):
        lista = comunicados_global.objects.all()
        print(lista)
        return render(request, "directivo/lista.html", {'lista':lista})

#eEliminar comunicado#Directivo
class delete_comu(DeleteView):
    model= comunicados_global
    success_url = reverse_lazy('list-comunicado')


#editar comunicado#Directivo
class edit_comunicado(UpdateView):
   model = comunicados_global
   fields = ['title','description', 'archivo']
   template_name = 'directivo/edit-comu.html'
   #template_name_suffix = '_update_form'

   def get_success_url(self):
    return reverse_lazy('edit-comu', args=[self.object.id])






def subirextra(request):
    if request.method == 'POST':
        form = ComunicadoExtraform(request.POST, request.FILES)
        if form.is_valid():
            newdoc = comunicadoescolar(title = request.POST['title'],description = request.POST['description'],image = request.FILES['image'],categoria = request.POST["categoria"])
            newdoc.save(form)
            return redirect("subirextra")
    else:
        form = ComunicadoExtraform()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'siscontrol/subirextra.html', {'form': form})

class admin_extra(ListView):
    model=comunicadoescolar

    def get(self,request,*args,**kwars):
        cate = request.user.categoria
        #print(turno)
        comunicado = comunicadoescolar.objects.filter(categoria=cate)
        #print(comunicado)
    
        return render(request, "comunicados_global_list/comunicados_global_extra.html", {'comunicado':comunicado})


class delete_extra(DeleteView):
    model= comunicadoescolar
    success_url = reverse_lazy('admin_extra')



###############horarios#########################
class horario(ListView):
    model = horarios

    def get(self, request, *args, **kwargs):
        gra = request.user.grado
        gru = request.user.grupo
        obj = horarios.objects.filter(grupo=gru ,grado=gra)
        print(obj)
        return render(request, "horarios/horarios.html", {'obj':obj})

class list_horarios(ListView):
    model = horarios

    def get(self,request,*args,**kwargs):
        horario = horarios.objects.all()
        return render(request, "horarios/list-horarios.html", {'horario':horario})

def delete_horario(request):
    hora = horarios.objects.all().delete()
    return render(request,"horarios/list-horarios.html")

    def get_success_url(self):
        return reverse_lazy('list_horarios') + '?delete'
    



    


        
#####################################SUBIR EXCEL###########################################
######generar pdf's######

def forma(request):
    return render(request, "inscripciones/formato.html")

def pag(request):
    return render(request, "inscripciones/pago.html")

def convo(request):
    return render(request, "inscripciones/convocatoria.html")

def nuevo(request):
    
    return render(request, "inscripciones/nuevo.html")

def cursador(request):
    return render(request, "inscripciones/cursadores.html")
    
def normal(request):
    return render(request, "inscripciones/normal.html")

def repite(request):
    return render(request, "inscripciones/repetidor.html")






  