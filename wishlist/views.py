from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Rakan Fasya Athhar Rayyan'
    }
    return render(request, "wishlist.html", context)

def return_XML(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def return_JSON(request):
    data = BarangWishlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def return_ID(request, id):
    data = BarangWishlist.objects.filter(pk=id)

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")