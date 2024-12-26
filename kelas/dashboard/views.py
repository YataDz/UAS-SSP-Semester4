
from dashboard.forms import FormBarang
from dashboard.forms import FormBarang2
from dashboard.models import *
from django.contrib import messages
from django.shortcuts import render,redirect
# Create your views here.

def beranda(request):
    titelnya="Beranda"
    konteks = {
        'titel' : titelnya,
    }
    return render(request,"beranda.html",konteks)


def beli_barang(request):
    if request.POST:
        form=FormBarang(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            print(request.FILES)
            form.save()
            messages.success(request,"Data Pembelian Berhasil Ditambahkan")
            form = FormBarang()
            konteks = {
                'form':form,
        }
        return render(request,'beli_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,"beli_barang.html",konteks)


def jual_barang(request):
    if request.POST:
        form=FormBarang2(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            print(request.FILES)
            form.save()
            messages.success(request,"Data Penjualan Berhasil Ditambahkan")
            form = FormBarang2()
            konteks = {
                'form':form,
        }
        return render(request,'jual_barang.html',konteks)
    else:
        form=FormBarang2()
        konteks = {
            'form':form,
        }
    return render(request,"jual_barang.html",konteks)


def Barang_View(request):
    barang_beli=Barangbeli.objects.all()
    barang_jual=Barangjual.objects.all()

    konteks={
        'barang_beli':barang_beli,
        'barang_jual':barang_jual,
    }
    return render (request,'tampil_data.html',konteks)


def beli_ubah(request,id_barang):
    barangs=Barangbeli.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST, request.FILES, instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil di ubah")
            return redirect('ubah_beli',id_barang=id_barang)

    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'forms':form,
            'barangs':barangs
        }    
    return render(request,'ubah_beli.html',konteks)


def jual_ubah(request,id_barang):
    barangss=Barangjual.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang2(request.POST, request.FILES,instance=barangss)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil di ubah")
            return redirect('ubah_jual',id_barang=id_barang)

    else:
        form=FormBarang2(instance=barangss)
        konteks = {
            'forms':form,
            'barangss':barangss
        }    
    return render(request,'ubah_jual.html',konteks)



def hapus_brg(request, id_barang):
    barangs=Barangbeli.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('Vbrg')

def hapus_brg_jual(request, id_barang):
    barangs=Barangjual.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request, "Data Terhapus")
    return redirect('Vbrg')

