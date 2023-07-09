from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from product.models import Airvehicles,Category
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostIHAForm
from django_serverside_datatable.views import ServerSideDatatableView
from django.utils.safestring import mark_safe




# Create your views here.
def index(request):
    context = {
       "vehicles": Airvehicles.objects.filter(is_active=True),
       "categories":Category.objects.all()
    }
    return render(request, "iha/index.html", context)

def categories(request):
    context = {
       "vehicles": Airvehicles.objects.filter(is_active=True), #Aktif olan kayıtları filitre ediyoruz.
       "categories":Category.objects.all()
    }
    return render(request, "iha/categories.html", context)

def iha_details(request, slug):
    
    context = {
       "vehicle" : Airvehicles.objects.get(slug=slug),
        "categories":Category.objects.all()
    } 
    return render(request, "iha/iha_details.html",context)
    
def iha_categoriy(request, slug):
   context = {
       "vehicles": Category.objects.get(slug=slug).airvehicles_set.filter(is_active=True), #ilişkili olan kayıtları kategoriye göre listeliyoruz
       # "vehicles": Airvehicles.objects.filter(is_active=True, category__slug=slug), #ilişkili olan kayıtları kategori parametre olarak slug bilgisine göre listeliyoruz 
       "categories":Category.objects.all(),
       "categoriinfo":Category.objects.get(slug=slug),
    }
   return render(request, "iha/index.html", context)

def iha_datatable(request):
    context = {
       "vehicles": Airvehicles.objects.filter(is_active=True),
       "categories":Category.objects.all()
    }
    return render(request, "iha/index.html", context)

def iha_datatable_index(request):
    form = PostIHAForm(request.POST or None, request.FILES or None)
    context = {
        'form': form,
        "vehicles": Airvehicles.objects.filter(is_active=True),
        "categories":Category.objects.all(),
    }
    return render(request, "iha/iha-datatable.html", context)  

def iha_update(request,slug):
    form = PostIHAForm(request.POST or None, request.FILES or None,instance=Airvehicles.objects.get(slug=slug))
    if form.is_valid():
        post = form.save(commit=False)
        post.save()   
        messages.success(request, "Başarılı bir şekilde güncellediniz.") 
        return HttpResponseRedirect("/iha/iha-lists")

    
    context = {
       "form" : form,
        "categories":Category.objects.all()
    } 
    
    return render(request, "iha/iha_update.html",context)

def post_iha_delete(request, slug):
    post = get_object_or_404(Airvehicles, slug=slug)
    post.delete()
    return HttpResponseRedirect("/iha/iha-lists")
    
def post_iha_create(request):

    form = PostIHAForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        messages.success(request, "Başarılı bir şekilde oluşturdunuz.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect("/iha/iha-lists")

    context = {
        'form': form,
        "categories":Category.objects.all()
    }

    return render(request, "iha/form.html", context)