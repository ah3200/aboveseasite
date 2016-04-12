from rest_framework import serializers

from blogengine.models import User, Story, Photo

class UserSerializer(serializers.ModelSerializer):
#    stories = serializers.HyperlinkedIdentityField(view_name='userstory-list', lookup_field='username')
    stories = serializers.PrimaryKeyRelatedField(many=True, queryset=Story.objects.all())
    
    class Meta:
        model = User
        field = ('id','username','email','first_name','last_name','stories')
        
class StorySerializer(serializers.ModelSerializer):
    authoer = UserSerializer(required=False)
    
    class Meta:
        model = Story

class PhotoSerializer(serializers.ModelSerializer):
#    image = serializers.Field('image.url')

    class Meta:
        model = Photo