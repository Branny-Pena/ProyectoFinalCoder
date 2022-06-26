from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso, Estudiante, Profesor
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
# Create your views here.
def inicio(request):
    return render(request,"ProyectoFinalApp/index.html")




def estudiantes(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            estudiantes = Estudiante.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"ProyectoFinalApp/estudiantes.html",{"estudiantes":estudiantes, "search":True, "busqueda":search})

    estudiantes = Estudiante.objects.all()

    return render(request,"ProyectoFinalApp/estudiantes.html",{"estudiantes":estudiantes})

def crear_estudiante(request):
    
    
    if request.method == "POST":
        
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            estudiante = Estudiante(nombre=info["nombre"],apellido=info["apellido"],email=info["email"])
            estudiante.save()

            return redirect("estudiantes")

        return render(request,"ProyectoFinalApp/formulario_estudiante.html",{"form":formulario})

    
    formulario = EstudianteFormulario()
    return render(request,"ProyectoFinalApp/formulario_estudiante.html",{"form":formulario})

def eliminar_estudiante(request,estudiante_id):

    estudiante = Estudiante.objects.get(id=estudiante_id)
    estudiante.delete()

    return redirect("estudiantes")

def editar_estudiante(request,estudiante_id):

    estudiante = Estudiante.objects.get(id=estudiante_id)

    if request.method == "POST":

        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            
            info_estudiante = formulario.cleaned_data
            
            estudiante.nombre = info_estudiante["nombre"]
            estudiante.apellido = info_estudiante["apellido"]
            estudiante.email = info_estudiante["email"]
            estudiante.save()

            return redirect("estudiantes")

    # get
    formulario = EstudianteFormulario(initial={"nombre":estudiante.nombre, "apellido":estudiante.apellido, "email": estudiante.email})
    
    return render(request,"ProyectoFinalApp/formulario_estudiante.html",{"form":formulario})


def profesores(request):

    profesores = Profesor.objects.all()

    return render(request,"ProyectoFinalApp/profesores.html",{"profesores":profesores})

class ProfesList(ListView):

    model = Profesor
    template_name = "ProyectoFinalApp/profesores_list.html"


class ProfeDetail(DetailView):

    model = Profesor
    template_name = "ProyectoFinalApp/profesor_detail.html"


class ProfeCreate(CreateView):

    model = Profesor
    success_url = "/finalapp/list"
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeUpdate(UpdateView):

    model = Profesor
    success_url = "/finalapp/list"
    fields = ["nombre", "apellido", "email", "profesion"]

class ProfeDelete(DeleteView):

    model = Profesor
    success_url = "/finalapp/list"



def cursos(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            cursos = Curso.objects.filter( Q(nombre__icontains=search) | Q(comision__icontains=search) ).values()

            return render(request,"ProyectoFinalApp/cursos.html",{"cursos":cursos, "search":True, "busqueda":search})
    cursos = Curso.objects.all()
    return render(request,"ProyectoFinalApp/cursos.html",{"cursos":cursos, "search":False})

def crear_curso(request):

    
    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso = Curso(nombre=info_curso["nombre"], comision=info_curso["comision"])
            curso.save() 
            
            return redirect("curso")

        else:

            return render(request,"ProyectoFinalApp/formulario_curso.html",{"form":formulario,"accion":"Crear Curso"})
    

    else: 

        formularioVacio = NuevoCurso()

        return render(request,"ProyectoFinalApp/formulario_curso.html",{"form":formularioVacio,"accion":"Crear Curso"})

def eliminar_curso(request, curso_id):

    
    curso = Curso.objects.get(id=curso_id)
    curso.delete()

    return redirect("curso")

def editar_curso(request, curso_id):

    curso = Curso.objects.get(id=curso_id)

    if request.method == "POST":

        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():

            info_curso = formulario.cleaned_data
        
            curso.nombre = info_curso["nombre"]
            curso.comision = info_curso["comision"]
            curso.save() 
            
            return redirect("curso")

            
    formulario = NuevoCurso(initial={"nombre":curso.nombre,"comision":curso.comision})

    return render(request,"ProyectoFinalApp/formulario_curso.html",{"form":formulario,"accion":"Editar Curso"})

def base(request):
    return render(request,"ProyectoFinalApp/base.html",{})




































