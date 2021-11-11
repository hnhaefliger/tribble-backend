from rest_framework import serializers

import os
import uuid

from .models import Session


class SessionSerializer(serializers.Serializer):
    '''
    Serializer for the ticker class.
    '''
    data = serializers.CharField()

    def create(self, validated_data):
        return Session.objects.create(
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
