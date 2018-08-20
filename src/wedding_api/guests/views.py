from django.shortcuts import render

from rest_framework import viewsets, filters


from . import serializers
from . import models
# Create your views here.


class GuestViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.GuestSerializer
    queryset = models.Guest.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
