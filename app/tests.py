from django.test import TestCase, Client, override_settings
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core import mail
from django.contrib.auth import get_user_model
from .models import Arrangement, Furniture

User = get_user_model()

# class ArrangementFurnitureTestCase(TestCase):
#     def setUp(self):
#         # Créer une instance d'Arrangement
#         self.arrangement = Arrangement.objects.create(
#             title='Test Arrangement',
#             description='Description de test',
#             main_picture=SimpleUploadedFile('main_image.jpg', b'file_content', content_type='image/jpeg'),
#         )
#         # Créer une instance de Furniture
#         self.furniture = Furniture.objects.create(
#             title='Test Furniture',
#             description='Description de test',
#             main_picture=SimpleUploadedFile('main_image.jpg', b'file_content', content_type='image/jpeg'),
#         )
#         self.client = Client()

#     def test_arrangement_creation(self):
#         """Test pour vérifier que l'arrangement a bien été créé et le main_picture est obligatoire"""
#         self.assertEqual(self.arrangement.title, 'Test Arrangement')
#         self.assertIsNotNone(self.arrangement.main_picture)

#     def test_furniture_creation(self):
#         """Test pour vérifier que le furniture a bien été créé et le main_picture est obligatoire"""
#         self.assertEqual(self.furniture.title, 'Test Furniture')
#         self.assertIsNotNone(self.furniture.main_picture)
        
#     def test_arrangements_pagination(self):
#         """Test de la pagination pour la vue des arrangements"""
#         url = reverse('arrangements')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.arrangement.title)

#     def test_furnitures_pagination(self):
#         """Test de la pagination pour la vue des furnitures"""
#         url = reverse('furnitures')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, self.furniture.title)

@override_settings(RECAPTCHA_PUBLIC_KEY='test-key', RECAPTCHA_PRIVATE_KEY='test-key')        
class ContactFormTestCase(TestCase):
  def setUp(self):
    # Crée un utilisateur 'Louis' avec une adresse email valide
    User = get_user_model()
    self.user = User.objects.create_user(
      username='username',
      first_name='Louis',
      email='louis@example.com',
      password='testpassword'
      )

  def test_contact_form_valid(self):
    """Test pour vérifier que le formulaire de contact fonctionne et envoie un email"""
    response = self.client.post(reverse('contact'), {
      'name': 'John Doe',
      'email': 'johndoe@example.com',
      'subject': 'Test Subject',
      'message': 'Test message content',
      'g-recaptcha-response': 'test-response'
    })

    print(response.content.decode())

    # Vérifie que le formulaire est validé
    self.assertEqual(response.status_code, 200)

    # Vérifie que l'e-mail a bien été envoyé
    self.assertEqual(len(mail.outbox), 1)
    self.assertEqual(mail.outbox[0].subject, 'Test Subject')

    # Vérifie que le message de succès est présent dans la réponse
    self.assertContains(response, "Votre message a été envoyé avec succès.")
    
  def test_contact_form_invalid(self):
    """Test pour vérifier que le formulaire ne soumet pas si le formulaire est invalide"""
    response = self.client.post(reverse('contact'), {
        'name': '',
        'email': '',
        'subject': '',
        'message': ''
    })
    self.assertFormError(response, 'form', 'name', 'Ce champ est obligatoire.')
    self.assertFormError(response, 'form', 'email', 'Ce champ est obligatoire.')
    self.assertFormError(response, 'form', 'subject', 'Ce champ est obligatoire.')
    self.assertFormError(response, 'form', 'message', 'Ce champ est obligatoire.')
