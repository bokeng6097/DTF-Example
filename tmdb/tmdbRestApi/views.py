from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Photo
from .serializers import PhotoSerializer

# Create your views here.

@api_view(['GET', ])
def api_list_photo_view(request):

    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET', ])
def api_detail_photo_view(request, pk):

    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PhotoSerializer(photo, context={'request': request})
        return Response(serializer.data)

@api_view(['POST', ])
def api_create_photo_view(request):

    if request.method == "POST":
        serializer = PhotoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
def api_update_photo_view(request, pk):

    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = PhotoSerializer(photo, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', ])
def api_delete_photo_view(request, pk):

    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        photo.delete()
        return Response(status=204)