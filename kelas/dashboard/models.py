from django.db import models

# Create your models here.
class Jenis(models.Model):
    id = models.AutoField(primary_key=1)
    nama=models.CharField(max_length=50)
    ket=models.TextField()
    
    def __str__(self):
        return self.nama

id = models.AutoField(primary_key=1)

class Barangbeli(models.Model):
    id = models.AutoField(primary_key=1)
    kodeworld = models.CharField(verbose_name='World', max_length=10)
    nama = models.CharField(max_length=50)
    growid = models.CharField(max_length=8)
    nomor = models.BigIntegerField(verbose_name='Nomor Rekening')
    jumlah = models.IntegerField()
    pembayaran=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
    buktitransfer=models.ImageField(verbose_name='Bukti Transfer',upload_to='images/', blank=True)


class Barangjual(models.Model):
    id = models.AutoField(primary_key=1)
    jumlah = models.IntegerField()
    nomor = models.BigIntegerField()
    nama = models.CharField(max_length=50)
    nomor_rekening = models.BigIntegerField()
    pembayaran=models.ForeignKey(Jenis, on_delete=models.CASCADE,null=True)
    buktipengiriman=models.ImageField(verbose_name='Bukti Pengiriman',upload_to='images/', blank=True)