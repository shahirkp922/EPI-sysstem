from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    dict_eve={
        'post':Post.objects.all()
    }
    return render(request,'index.html',dict_eve)

def about(request):
    return render(request,'about.html')
