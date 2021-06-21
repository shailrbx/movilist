from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import movies
from .forms import movieform
# Create your views here.

def index(request):

    movie=movies.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def deails(request,nomov):
    movi=movies.objects.get(id=nomov)
    return  render(request,"details.html",{'movie':movi})

def add(request):
    if request.method == "POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        image = request.FILES['image']
        movie=movies(name=name, desc=desc, year=year, image=image)
        movie.save()
        print("added")


    return render(request, 'add_movi.html')

def update(request,id):
    movi=movies.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=movi)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html', {'form':form,'movi':movi})
def delete(request,id):
    if request.method=='POST':
        movi=movies.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')
