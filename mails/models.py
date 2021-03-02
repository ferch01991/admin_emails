from django.db import models

# Create your models here.

class Mail(models.Model):
    subject = models.CharField(max_length=50) #titulo del correo 
    content = models.TextField() #contenido del correo 
    created_at = models.DateTimeField(auto_now_add=True) # fecha cuando fue creado

    def __str__(self):
        return self.subject