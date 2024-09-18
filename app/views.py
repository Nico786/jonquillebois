import logging
from django.db import DatabaseError
from django.http import HttpResponseServerError
from django.shortcuts import render
from app.models import Arrangement

logger = logging.getLogger(__name__)

def home(request):
  return render(request, 'home.html')

def arrangement(request):
  try:
    arrangements = Arrangement.objects.all()
    if not arrangements.exists():
      logger.warning("Aucune instance d'agencement trouvée dans la base de données.")
      return render(request, 'arrangements.html', {'error': "Aucune réalisation n'a encore été ajoutée."})
    return render(request, 'arrangements.html', {'arrangements': arrangements})
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