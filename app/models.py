from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, TextField, ImageField

class CustomUser(AbstractUser):
  phone = CharField(max_length=15, unique=True, null=True, blank=True, default="")

  def __str__(self):
    return self.username
  

class Realisation(Model):
  title = CharField(max_length=100, blank=True, default="", verbose_name="Titre")
  description = TextField(blank=True, null=True, default="", verbose_name="Description")
  picture = ImageField(upload_to='images/', blank=True, null=True, verbose_name="Photo")
    
  class Meta:
    abstract = True

  def __str__(self):
    return self.title

class Arrangement(Realisation):
  class Meta:
    verbose_name = "Agencement"

class Furniture(Realisation):
  class Meta:
    verbose_name = "Mobilier"