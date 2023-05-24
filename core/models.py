from django.db import models

class Categorias(models.Model):
    nome = models.CharField('categoria', max_length=100)

    def __str__(self):
        return self.nome

class Foto(models.Model):
    foto = models.ImageField(upload_to='pics')
    categoria = models.ForeignKey('Categorias', on_delete=models.CASCADE)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return str(self.foto).replace('Foto: pics/', '')

class SobreMim(models.Model):
    foto = models.ImageField(upload_to='pics/sobremim')
    descricao = models.TextField()

class CamposAlteraveis(models.Model):
    nome_campo = models.CharField(max_length=60)
    texto_campo = models.TextField()

    def __str__(self):
        return self.nome_campo

