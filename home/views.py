from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from src.notebook.notebook import college_names,Branch_names,Categories_names
def home(request):
    return render(request,"base.html", {"college_names": college_names,"Branch_names":Branch_names,"Categories_names":Categories_names})
