from django.shortcuts import render
from .models import furniture


# Create your views here.
def home(request):
    obj = furniture.objects.all()
    return render(request, 'index.html', {'object': obj})


def shop(request, item_id):
    cart_item = furniture.objects.get(id=item_id)
    return render(request, 'shop.html', {'c_item': cart_item})


def cart(request, cart_id):
    crt_item = furniture.objects.get(id=cart_id)
    return render(request, 'cart.html', {'item_id': crt_item})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        img = request.FILES['img']
        material = request.POST.get('material')
        desc = request.POST.get('desc')
        prd = furniture(name=name,price=price,img=img,material=material,desc=desc)
        prd.save()
        print('product added..!')
    return render(request, 'add_product.html')
