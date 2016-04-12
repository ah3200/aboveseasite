from rest_framework import viewsets, permissions, renderers

from blogengine.models import User, Story, Photo
from blogengine.serializers import UserSerializer, StorySerializer, PhotoSerializer
from blogengine.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class StoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
                          
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    