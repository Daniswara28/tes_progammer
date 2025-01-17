from django.shortcuts import render
from .models import Produk

def produk_list(request):
    # Ambil semua produk dari database
    produk = Produk.objects.all()
    return render(request, 'produk/produk_list.html', {'produk': produk})
