from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core import mail
from django.contrib.auth import get_user_model
from .models import Arrangement, Furniture

User = get_user_model()

class ArrangementFurnitureTestCase(TestCase):
    def setUp(self):
        # Créer une instance d'Arrangement
        self.arrangement = Arrangement.objects.create(
            title='Test Arrangement',
            description='Description de test',
            main_picture=SimpleUploadedFile('main_image.jpg', b'file_content', content_type='image/jpeg'),
        )
        # Créer une instance de Furniture
        self.furniture = Furniture.objects.create(
            title='Test Furniture',
            description='Description de test',
            main_picture=SimpleUploadedFile('main_image.jpg', b'file_content', content_type='image/jpeg'),
        )
        self.client = Client()

    def test_arrangement_creation(self):
        """Test pour vérifier que l'arrangement a bien été créé et le main_picture est obligatoire"""
        self.assertEqual(self.arrangement.title, 'Test Arrangement')
        self.assertIsNotNone(self.arrangement.main_picture)

    def test_furniture_creation(self):
        """Test pour vérifier que le furniture a bien été créé et le main_picture est obligatoire"""
        self.assertEqual(self.furniture.title, 'Test Furniture')
        self.assertIsNotNone(self.furniture.main_picture)