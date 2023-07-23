from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal

from coffeshop.products.models import Category, Product


UserModel = get_user_model()


class ProductDetailsViewTestCase(TestCase):
    def setUp(self):
        # Create a test Category and Product
        self.user = UserModel.objects.create_user(username='testuser', password='Testpass123!')
        self.category = Category.objects.create(name='Test Category', status=0)
        # Create a Django test client
        self.client = Client()

    def test_create_product(self):
        self.product = Product.objects.create(name='Test Product', price=Decimal(3.45), category=self.category,
                                              quantity=10, status=0)

    def test_invalid_product(self):
        url = reverse('product details', args=['Test Category', 'Non-Existent Product'])
        response = self.client.get(url)

        # Assert that the response redirects to the catalogue page
        self.assertRedirects(response, reverse('catalogue'))

        # Assert that the correct error message is displayed
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No such Product found')

    def test_invalid_category(self):
        url = reverse('product details', args=['Non-Existent Category', 'Test Product'])
        response = self.client.get(url)

        # Assert that the response redirects to the catalogue page
        self.assertRedirects(response, reverse('catalogue'))

        # Assert that the correct error message is displayed
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No such Category found')

    def test_invalid_category_and_product(self):
        url = reverse('product details', args=['Non-Existent Category', 'Non-Existent Product'])
        response = self.client.get(url)

        # Assert that the response redirects to the catalogue page
        self.assertRedirects(response, reverse('catalogue'))

        # Assert that the correct error message is displayed
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'No such Category found')