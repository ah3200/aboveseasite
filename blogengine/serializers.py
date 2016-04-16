from rest_framework import serializers

from blogengine.models import User, Story, Photo
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
#    stories = serializers.HyperlinkedIdentityField(view_name='userstory-list', lookup_field='username')
    stories = serializers.PrimaryKeyRelatedField(many=True, queryset=Story.objects.all())
    
    class Meta:
        model = User
        fields = ('id','username','email','first_name','last_name','stories')
        
class StorySerializer(TaggitSerializer, serializers.ModelSerializer):
    author = UserSerializer(required=False)
    tags = TagListSerializerField()
    
    class Meta:
        model = Story

class PhotoSerializer(serializers.ModelSerializer):
#    image = serializers.Field('image.url')

    class Meta:
        model = Photo