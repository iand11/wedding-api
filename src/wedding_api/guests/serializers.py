from rest_framework import serializers

from . import models


class GuestSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Guest
        fields = ('name', 'email', 'is_coming', 'people_attending')
        extra_kwargs = {'name': {'read_only': True}, 'email': {'allow_null': True}, 'people_attending': {'allow_null': True}}