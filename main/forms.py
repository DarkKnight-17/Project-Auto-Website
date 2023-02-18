from .models import Services, Auto_parts, Car
from django.forms import ModelForm ,TextInput, IntegerField

class Carform(ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['user']

class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        exclude = ['user']

class Auto_partsForm(ModelForm):
    class Meta:
        model = Auto_parts
        fields = '__all__'
        exclude = ['user']