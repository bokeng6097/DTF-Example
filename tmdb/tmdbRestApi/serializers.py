from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
        
    class Meta:

        model = Photo
        fields = ['id', 'title', 'description', 'filename', 'image', 'oriLink']

















# =============================================================================
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=100)
#     filename = serializers.CharField(max_length=100)
#     oriLink = serializers.CharField(max_length=100)
#      
#     def create(self, validated_data):
#         return Article.objects.create(validated_data)
#      
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.filename = validated_data.get('filename', instance.filename)
#         instance.oriLink = validated_data.get('oriLink', instance.title)
#         instance.save()
#         return instance
# =============================================================================
