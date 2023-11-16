from django.shortcuts import render
from .models import furniture


# Create your views here.
def home(request):
    obj = furniture.objects.all()
    return render(request, 'index.html', {'object': obj})


def shop(request, item_id):
    cart_item = furniture.objects.get(id=item_id)
    return render(request, 'shop.html', {'c_item': cart_item})
