from django.db import models

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name='Nombre', null=False, blank=False)
    description = models.CharField(max_length=255, verbose_name='Descripción', null=False, blank=False)
    create_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name= 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Book(models.Model):
    title= models.CharField(max_length=150, verbose_name='Titulo', null=False, blank=False)
    description= models.CharField(max_length=255, verbose_name='Descripción', null=False, blank=False)
    author= models.CharField(max_length=100, verbose_name='Autor', null=False, blank=False)
    year= models.CharField(max_length=4, verbose_name='Año', null=False, blank=False)
    front= models.ImageField(default=None, verbose_name='Portada', null=False, blank=False, upload_to='portadas')
    categories= models.ManyToManyField(Category, verbose_name='Categorías', null=False, blank=False, related_name="books")

    class Meta:
        verbose_name= 'Libro'
        verbose_name_plural = 'Libros'
