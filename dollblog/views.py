from django.shortcuts import render
from django.http import HttpResponse
# from . import dummyposts
from .models import Post, Doll

context = {
    'posts': Post.objects.all()
}

# Create your views here.
def home(request):
    #return HttpResponse('<h1> Blog Home</h1>')
    return render(request, 'dollhome.html', context)

def about(request):
    #return HttpResponse('<h1> Blog-About</h1>')
    return render(request, 'dollabout.html', {'title': 'About'})