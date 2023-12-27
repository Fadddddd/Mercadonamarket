from django.test import TestCase
from django.urls import reverse
from merchandise.models import Category, Product
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

def create_image():
    # Create a simple image in memory
    image = Image.new('RGB', (100, 100), 'white')
    buffer = BytesIO()
    image.save(buffer, format='JPEG')
    image_file = SimpleUploadedFile("test.jpg", buffer.getvalue())
    return image_file

class MerchandiseViewsTest(TestCase):
    def setUp(self):
        # Create objects Category and Product for tests
        self.category = Category.objects.create(libelle='Test Category')
        self.product = Product.objects.create(
            libelle='Test Product',
            description='Test Description',
            price=19.99,
            category=self.category,
            image=create_image()
        )
    # def test_accueil_view(self):
    #     url = reverse('accueil')
    #     response = self.client.get(url)

    #     # Check that the view returns a code 200
    #     self.assertEqual(response.status_code, 200)
    #     print(response.context)

    #     # Check that the context contains products and categories
    #     self.assertIn('products', response.context)
    #     self.assertIn('categories', response.context)

    def test_products_view(self):
        url = reverse('products')
        response = self.client.get(url)

        # Check that the view returns a code 200
        self.assertEqual(response.status_code, 200)

        # Check that the context contains products
        self.assertIn('products', response.context)

    def test_search_view(self):
        url = reverse('search')
        response = self.client.get(url, {'q': 'Test'})

        # Check that the view returns a code 200
        self.assertEqual(response.status_code, 200)

        # Check that the context contains products and the search query
        self.assertIn('products', response.context)
        self.assertIn('query', response.context)

    def test_category_product_list_view(self):
        # Use reverse with the category id
        url = reverse('category_product_list', args=[str(self.category.id)])
        response = self.client.get(url)

        # Check that the view returns a code 200
        self.assertEqual(response.status_code, 200)

        # Check that the context contains the category and associated products
        self.assertIn('category', response.context)
        self.assertIn('products', response.context)
