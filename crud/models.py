from django.db import models

# Create your models here.
class Marca(models.Model):
    marca = models.CharField(verbose_name='Marca', max_length=50)
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'
        ordering = ['marca']

    def __str__(self) -> str:
        return self.marca


class Joyeria(models.Model):
    idJoyeria = models.CharField(primary_key=True,verbose_name='ID',max_length=20)
    name = models.CharField(verbose_name='Nombre',max_length=250)
    tipo = models.CharField(verbose_name='Tipo de Joya',max_length=100)
    marca = models.ForeignKey(Marca,verbose_name='Marca',on_delete=models.CASCADE)
    value = models.IntegerField(verbose_name='Valor')
    stock = models.IntegerField(verbose_name='Stock')
    image = models.ImageField(verbose_name='Imagen',upload_to='joyeria',null=True,blank=True)    
    created_at = models.DateTimeField(verbose_name='Fecha creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización', auto_now=True)

    class Meta:
        verbose_name = 'joyeria'
        verbose_name_plural = 'joyerias'
        ordering = ['idJoyeria']

    def __str__(self) -> str:
        return self.name
