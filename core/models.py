from django.db import models

class Categorias(models.Model):
    nome = models.CharField('categoria', max_length=100)

    def __str__(self):
        return self.nome

class Foto(models.Model):
    foto = models.ImageField(upload_to='pics')
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE)

class SobreMim(models.Model):
    foto = models.ImageField(upload_to='pics/sobremim')
    descricao = models.TextField()