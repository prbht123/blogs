from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post,Category




class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields=['id','title','slug','body','status','author','category',]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['id','category_name','slug']