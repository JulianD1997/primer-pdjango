from django.db import models

# Create your models here.
"""En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y 
luego se puedan ver sus películas, así como una descripción de las mismas
Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes de la aplicación."""

class Gender(models.Model):
    name = models.CharField(max_length=60,help_text="Introduce el genero")

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=70,help_text="Introduce el nombre del director")
    last_name = models.CharField(max_length=70,help_text="Introduce el apellido del director")
    date_of_birth = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    title = models.CharField(max_length=50,help_text="Introduce el nombre de la pelicula")
    director = models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)         
    gender = models.ManyToManyField(Gender)
    summary = models.TextField(max_length=100,help_text="Sinopsis de la pelicula")
    premier = models.DateField(null=True)
    def __str__(self):
        return self.title