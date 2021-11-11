from rest_framework import serializers
from django.core import exceptions

import os
import uuid

from .models import Session


def validate_name(name):
    if len(name) < 1 or len(name) > 128:
        raise exceptions.ValidationError('Invalid name length.')


def validate_description(description):
    if len(description) < 32 or len(description) > 512:
        raise exceptions.ValidationError('Invalid description length.')


class SessionSerializer(serializers.Serializer):
    name = serializers.CharField(validators=(validate_name,))
    description = serializers.CharField(validators=(validate_description,))
    data = serializers.CharField()

    def create(self, validated_data):
        return Session.objects.create(
            name = validated_data['name'],
            description = validated_data['description'],
            location = validated_data['location'],
        )

    def validate(self, data):
        location = 'session_store/' + str(uuid.uuid4()) + '.txt'

        try:
            with open(location, 'w+') as f:
                f.write(data['data'])

        except:
            os.mkdir('session_store')

            with open(location, 'w+') as f:
                f.write(data['data'])

        data['location'] = location

        return data
