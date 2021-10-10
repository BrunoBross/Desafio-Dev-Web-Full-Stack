from django.db import models
from django.utils import timezone
from django import forms


class Number(models.Model):
    numbers = models.CharField(max_length=8)
    smallduodigit = models.CharField(max_length=8, default=0)
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.numbers


class FormVerificador(forms.ModelForm):
    class Meta:
        model = Number
        exclude = ('date_time', 'smallduodigit',)
