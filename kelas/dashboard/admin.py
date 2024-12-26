from django.contrib import admin

# Register your models here.
from .models import Barangbeli,Jenis,Barangjual


class kolomBarang(admin.ModelAdmin):
    list_display = ['kodeworld','nama','growid','nomor','jumlah','buktitransfer']
    search_fields = ['kodeworld','nama']
    list_filter=('pembayaran',)
    list_per_page= 3

class kolomBarangs(admin.ModelAdmin):
    list_display = ['jumlah','nomor','nama','nomor_rekening','buktipengiriman']
    search_fields = ['jumlah','nomor']
    list_filter=('pembayaran',)
    list_per_page= 3

admin.site.register(Barangbeli,kolomBarang)
admin.site.register(Barangjual,kolomBarangs)
admin.site.register(Jenis)