from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, ImageField, IntegerField
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
  phone = CharField(max_length=15, blank=True, default="")
  address = CharField(max_length=100, blank=True, default="")

  def __str__(self):
    return self.username
  

class Realisation(Model):
  title = CharField(max_length=100, blank=True, default="", verbose_name="Titre")
  description = TextField(blank=True, default="", verbose_name="Description")
  main_picture = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo principale")
  picture_2 = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo secondaire")
  picture_3 = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo secondaire")
  picture_4 = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo secondaire")
  picture_5 = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo secondaire")
  position = IntegerField(default=0)
    
  class Meta:
    abstract = True
    ordering = ['position']

  def __str__(self):
    return self.title
  
  def clean(self):
        super().clean()
        if not self.main_picture:
            raise ValidationError('Une photo principale (vignette) est requise pour valider la création.')

class Arrangement(Realisation):
  class Meta:
    ordering = ['position']
    verbose_name = "Agencement"

class Furniture(Realisation):
  class Meta:
    ordering = ['position']
    verbose_name = "Mobilier"