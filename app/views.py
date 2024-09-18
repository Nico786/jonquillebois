import logging
from django.db import DatabaseError
from django.http import HttpResponseServerError
from django.shortcuts import render

from app.models import Arrangement
from app.utils import paginate_objects

logger = logging.getLogger(__name__)

def home(request):
  return render(request, 'home.html')

def arrangement(request):
  try:
    arrangements_list = Arrangement.objects.all()
    page_obj = paginate_objects(request, arrangements_list, 9)
    if not arrangements_list.exists():
      logger.warning("Aucune instance d'agencement trouvée dans la base de données.")
      return render(request, 'arrangements.html', {'error': "Aucune réalisation n'a encore été ajoutée."})
    return render(request, 'arrangements.html', {'page_obj': page_obj})
  except DatabaseError as e:
      logger.error(f"Erreur de la base de données : {str(e)}")
      return HttpResponseServerError("Erreur de la base de données. Veuillez réessayer plus tard.")
  except Exception as e:
    logger.critical(f"Erreur inattendue : {str(e)}")
    return HttpResponseServerError(f"Erreur inattendue : {str(e)}")

def furnitures(request):
  return render(request, 'furnitures.html')

def contact(request):
  return render(request, 'contact.html')