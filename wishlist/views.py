import datetime
from email.policy import HTTP
from operator import methodcaller
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from requests import request
from wishlist.models import BarangWishlist

# Create your views here.
@login_required(login_url='/wishlist/login/')
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    var = request.COOKIES.get('last_login', 'UserNotFound')
    if var == "UserNotFound":
        response = HttpResponseRedirect(reverse("wishlist:login"))
        return response
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Rakan Fasya Athhar Rayyan',
        'last_login': var,
    }
    return render(request, "wishlist.html", context)

def add_wishlist(request) :
    if request.method == "POST":
        print("test")
        nama_barang = request.POST.get("nama_barang")
        harga_barang = request.POST.get("harga_barang")
        deskripsi_barang = request.POST.get("deskripsi_barang")
        BarangWishlist.objects.create(nama_barang=nama_barang, harga_barang=harga_barang, deskripsi_barang=deskripsi_barang)
        return HttpResponse()
    else :
        response = redirect("wishlist:show_wishlist")
        return response

@login_required(login_url='/wishlist/login/')
def show_ajax_wishlist(request):
    var = request.COOKIES.get('last_login', 'UserNotFound')
    if var == "UserNotFound":
        response = HttpResponseRedirect(reverse("wishlist:login"))
        return response
    context = {
        'nama': 'Rakan Fasya Athhar Rayyan',
        'last_login': var,
    }
    return render(request, "wishlist_ajax.html", context)

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("wishlist:show_wishlist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response