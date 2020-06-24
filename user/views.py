from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def create(request):
    name = "Ashish A K"
    number = [1,2,3,4,5]
    all_info = User.objects.all()

    args = {'name': name, 'array':number , 'users': all_info}
    return render(request, 'user-create.html', args)


def details(request):
    name = "Ashish A K"
    number = [1,2,3,4,5]
    all_info = User.objects.all()

    args = {'name': name, 'array':number , 'users': all_info}
    return render(request, 'user-detail.html', args)

def list(request):
    name = "Ashish A K"
    number = [1,2,3,4,5]
    all_info = User.objects.all()

    args = {'name': name, 'array':number , 'users': all_info}
    return render(request, 'user-list.html', args)