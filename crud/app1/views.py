from rest_framework import viewsets
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    