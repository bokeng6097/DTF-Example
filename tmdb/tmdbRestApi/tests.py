from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from six import BytesIO

from .models import Photo
from .serializers import PhotoSerializer

client = APIClient()

# Create your tests here.
class PhotoListTest(APITestCase):


    def setUp(self):

        image = self.generate_photo_file()

        Photo.objects.create(
            title='Phone One',
            description='Photo One Description',
            image=SimpleUploadedFile('image.jpg', image.getvalue()),
            oriLink="https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg"
            )
    
        Photo.objects.create(
            title='Photo Two',
            description='Photo Two Description',
            image=SimpleUploadedFile('image.jpg', image.getvalue()),
            oriLink="https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg",
            )

        Photo.objects.create(
            title='Photo Three',
            description='Photo Three Description',
            image=SimpleUploadedFile('image.jpg', image.getvalue()),
            oriLink="https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg",
            )
    
    def generate_photo_file(self):
        
        image = BytesIO()
        Image.new('RGB', (100, 100)).save(image, 'JPEG')
        image.seek(0)
        return image
    
    def test_get_all_photo(self):
        
        response = client.get('/photo/')
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True, context={'request': response.wsgi_request})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_valid_single_photo(self):
        
        response = client.get('/photo/1/')
        photo = Photo.objects.get(pk=1)
        serializer = PhotoSerializer(photo, context={'request': response.wsgi_request})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_get_invalid_single_photo(self):
        
        response = client.get('/photo/4/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_single_photo(self):

        image = self.generate_photo_file()

        valid_payload = {
            'title':'Phone Valid',
            'description':'Photo Valid Description',
            'image':SimpleUploadedFile('image.jpg', image.getvalue()),
            'oriLink':"https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg"
        }

        response = client.post('/create/', valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_single_photo(self):

        image = self.generate_photo_file()

        invalid_payload = {
            'title':'',
            'description':'Photo Valid Description',
            'image':SimpleUploadedFile('image.jpg', image.getvalue()),
            'oriLink':"https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg"
        }

        response = client.post('/create/', invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_valid_single_photo(self):

        image = self.generate_photo_file()

        valid_payload = {
            'title':'Phone Update',
            'description':'Photo Update Description',
            'image':SimpleUploadedFile('image.jpg', image.getvalue()),
            'oriLink':"https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg"
        }

        response = client.put('/photo/1/update/', format='multipart', data=valid_payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_invalid_single_photo(self):

        image = self.generate_photo_file()

        invalid_payload = {
            'title':'',
            'description':'Photo Update Description',
            'image':SimpleUploadedFile('image.jpg', image.getvalue()),
            'oriLink':"https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg"
        }

        response = client.put('/photo/1/update/', format='multipart', data=invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_valid_single_photo(self):
        
        response = client.delete('/photo/1/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_single_photo(self):
        
        response = client.delete('/photo/4/delete/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)