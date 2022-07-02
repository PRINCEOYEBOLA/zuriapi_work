from rest_framework import viewsets
from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer

# Create your views here.

class LinkListApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active =True)
    serializer_class = LinkSerializer
    

class LinkCreateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active =True)
    serializer_class = LinkSerializer


class LinkDetailApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active =True)
    serializer_class = LinkSerializer


class LinkUpdateApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active =True)
    serializer_class = LinkSerializer

class LinkDeleteApi(viewsets.ModelViewSet):
    queryset = Link.objects.filter(active =True)
    serializer_class = LinkSerializer


