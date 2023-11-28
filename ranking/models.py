from django.db import models
from django.conf import settings

class Bandeco(models.Model):
    name = models.CharField(max_length=255)
    horarios = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    img_url = models.URLField(default="")

class Item(models.Model):
    name = models.CharField(max_length=255)
    bandeco = models.ManyToManyField(Bandeco, through="Nota")

class Nota(models.Model):
    bandeco = models.ForeignKey(Bandeco, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField(default=0)

class Comentario(models.Model):
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    bandeco = models.ForeignKey(Bandeco, on_delete=models.CASCADE)
    nota = models.IntegerField(default=0)
