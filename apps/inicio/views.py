from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from apps.siscontrol.models import comunicadoescolar

# Create your views here.
def contact(request):
    return render(request, "contact/contact.html")
	

#vistas pestaña 1
def quinsom(request):
	obj = request.user.username
	print(obj)
	return render(request, "quinsom/quinsom.html")

def prop(request):
	return render(request, "quinsom/proposito.html")

def orga(request):
	return render(request, "quinsom/organigrama.html")

def mivi(request):
	return render(request, "quinsom/vimi.html")

def valo(request):
	return render(request, "quinsom/valores.html")

def equidir(request):
	return render(request, "quinsom/equidir.html")

def calen(request):
	return render(request, "quinsom/calendario.html")
#############Extraescolares#################
class comu_extra_dibujo(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="di")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_taekwondo(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="ta")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_hawaiano(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="ha")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_danza(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="da")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_marimba(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="ma")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_voca(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="vo")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_bandaguerra(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="bg")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_tochito(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="to")
        return render(request,"quinsom/extraescolar.html" , {'comunicado':comunicado})

class comu_extra_escolta(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="es")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_basquet(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="ba")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_futbol(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="fu")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

class comu_extra_voli(ListView):
    model = comunicadoescolar
    def get(self,request,*args,**kwargs):
        comunicado = comunicadoescolar.objects.filter(categoria="vo")
        return render(request, "quinsom/extraescolar.html", {'comunicado':comunicado})

#vista logeo


