from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Portfolio

# Create your tests here.

class PortfolioPhotoTests(TestCase):
    def test_photo_upload(self):
        # Create test image
        image_content = b'fake-image-content'
        photo = SimpleUploadedFile("test.jpg", image_content, content_type="image/jpeg")
        
        # Test upload
        portfolio = Portfolio.objects.create(
            photo=photo,
            # ... other required fields ...
        )
        self.assertTrue(portfolio.photo)
        self.assertIn('portfolio/', portfolio.photo.name)
