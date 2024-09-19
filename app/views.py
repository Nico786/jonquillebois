import logging
from django.db import DatabaseError
from django.core.mail import EmailMessage
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib import messages

from app.forms import ContactForm
from app.models import Arrangement, Furniture
from app.utils import paginate_objects

logger = logging.getLogger(__name__)

def get_paginated_objects(request, model_class, template_name, context_name, error_message):
  try:
    objects_list = model_class.objects.all()
    page_obj = paginate_objects(request, objects_list, 9)
    if not objects_list.exists():
      logger.warning(f"Aucune instance de {model_class.__name__.lower()} trouvée dans la base de données.")
      return render(request, template_name, {context_name: [], 'error': error_message})
    return render(request, template_name, {context_name: page_obj})
  except DatabaseError as e:
      logger.error(f"Erreur de la base de données : {str(e)}")
      return HttpResponseServerError("Erreur de la base de données. Veuillez réessayer plus tard.")
  except Exception as e:
      logger.critical(f"Erreur inattendue : {str(e)}")
      return HttpResponseServerError(f"Erreur inattendue : {str(e)}")

def get_object_detail(request, model_class, pk, template_name, context_name):
  try:
    obj = get_object_or_404(model_class, pk=pk)
    images = [obj.main_picture] + [obj.picture_2, obj.picture_3, obj.picture_4, obj.picture_5]
    images = [img for img in images if img]
    return render(request, template_name, {context_name: obj, 'images': images})
  except DatabaseError as e:
    logger.error(f"Erreur de la base de données : {str(e)}")
    return HttpResponseServerError("Erreur de la base de données. Veuillez réessayer plus tard.")
  except Exception as e:
    logger.critical(f"Erreur inattendue : {str(e)}")
    return HttpResponseServerError(f"Erreur inattendue : {str(e)}")
      
def arrangements(request):
  return get_paginated_objects(
    request,
    Arrangement,
    'arrangements.html',
    'page_obj',
    "Aucune réalisation n'a encore été ajoutée."
  )
    
def arrangement_detail(request, pk):
  return get_object_detail(
    request,
    Arrangement,
    pk,
    'arrangement_detail.html',
    'arrangement'
  )

def furnitures(request):
  return get_paginated_objects(
    request,
    Furniture,
    'furnitures.html',
    'page_obj',
    "Aucune réalisation n'a encore été ajoutée."
  )

def furniture_detail(request, pk):
  return get_object_detail(
    request,
    Furniture,
    pk,
    'furniture_detail.html',
    'furniture'
  )

def home(request):
  return render(request, 'home.html')

def contact(request):
  form = ContactForm(request.POST or None)
  user = get_user_model().objects.filter(first_name="Louis").first()
  
  if form.is_valid():
    name = form.cleaned_data['name']
    user_email = form.cleaned_data['email']  #mail de l'expediteur
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    full_message = f"Nom : {name}\nAdresse email : {user_email}\n\n{message}"
    
    if user and user.email:
        try:
          email = EmailMessage(
            subject,
            full_message,
            user_email,  # Expéditeur (visiteur)
            [user.email],  # Destinataire (user.email)
            headers={'Reply-To': user_email}  # Pour que les réponses aillent à l'email fourni
          )
          email.send(fail_silently=False)
          
          messages.success(request, "Votre message a été envoyé avec succès.")
        except Exception as e:
          messages.error(request, f"Erreur lors de l'envoi de l'email : {str(e)}")
          logger.exception(f"Erreur inattendue: {str(e)}")
    else:
      messages.error(request, "Impossible d'envoyer l'email pour le moment. Veuillez réessayer plus tard.")
      
  context = {
    'form': form,
    'phone': user.phone if user else '',
    'address': user.address if user else ''
  }
  return render(request, 'infos_contact.html', context)