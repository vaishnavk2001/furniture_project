from django.shortcuts import render
from .models import furniture


# Create your views here.
def home(request):
    obj = furniture.objects.all()
    return render(request, 'index.html', {'object': obj})
