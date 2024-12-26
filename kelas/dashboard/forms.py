from django.forms import ModelForm
from dashboard.models import Barangbeli
from dashboard.models import Barangjual
from django import forms

class FormBarang(ModelForm):
    class Meta:
        model=Barangbeli
        fields='__all__'

        widgets ={
            'kodeworld': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'growid': forms.TextInput({'class':'form-control'}),
            'nomor': forms.NumberInput({'class':'form-control'}),
            'jumlah': forms.NumberInput({'class':'form-control'}),
            'pembayaran': forms.Select({'class':'form-control'}),
            'buktitransfer': forms.ClearableFileInput(attrs={'class': 'form-control'}),

        }

class FormBarang2(ModelForm):
    class Meta:
        model=Barangjual
        fields='__all__'

        widgets ={
            'jumlah': forms.NumberInput({'class':'form-control'}),
            'nomor': forms.TextInput({'class':'form-control'}),
            'nama': forms.TextInput({'class':'form-control'}),
            'nomor_rekening': forms.NumberInput({'class':'form-control'}),
            'pembayaran': forms.Select({'class':'form-control'}),
            'buktipengiriman': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }