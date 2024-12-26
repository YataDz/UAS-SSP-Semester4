"""kelas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',beranda,name='home'),
    path('belibrg/',beli_barang),
    path('jualbrg/',jual_barang),
    path('Vbrg/',Barang_View, name='Vbrg'),
    path('ubah/<int:id_barang>',beli_ubah,name='ubah_beli'),
    path('ubah-jual/<int:id_barang>',jual_ubah,name='ubah_jual'),
    path('hapus/<int:id_barang>', hapus_brg,name='hapus_brg'),
    path('hapus_jual/<int:id_barang>', hapus_brg_jual,name='hapus_brg_jual')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
