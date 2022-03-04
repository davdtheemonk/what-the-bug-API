from rest_framework import serializers
from .models import Post,modules

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'pk',
            'title',
            'date',
            'location',
            'timetoread',
            'image',
            'post',
             ]

class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = modules
        fields = [
            'pk',
            'title',
            'post'
        ]

