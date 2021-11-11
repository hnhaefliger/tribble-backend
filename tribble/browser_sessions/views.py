from django.contrib.auth.hashers import make_password, check_password

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Session
from .serializers import SessionSerializer


class SessionViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'session'

    def get(self, request, *args, **kwargs):
        if 'offset' in request.GET:
            offset = int(request.GET['offset'])

        else:
            offset = 0

        if 'limit' in request.GET:
            limit = int(request.GET['limit'])

        else:
            limit = 20

        query_set = Session.objects.all()

        data = [{
            'id': session.id,
            'name': session.name,
            'description': session.description,
            'location': session.location,
            'submitted_at': session.submitted_at,
        } for session in query_set[offset:offset+limit]]

        return Response(data=data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            data = Session.objects.get(id=kwargs['session'])

            data = {
                'id': data.id,
                'name': data.name,
                'description': data.description,
                'location': data.location,
                'submitted_at': data.submitted_at,
            }

            with open(data['location'], 'r') as f:
                data['data'] = f.read()

            return Response(data=data, status=status.HTTP_200_OK)

        except:
            return Response(data={'error': 'session not found'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        serializer = SessionSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()

            data = {
                'id': data.id,
                'name': data.name,
                'description': data.description,
                'location': data.location,
                'submitted_at': data.submitted_at,
            }

            with open(data['location'], 'r') as f:
                data['data'] = f.read()

            return Response(data=data, status=status.HTTP_200_OK)

        else:
            return Response(data={
                'error': 'invalid data',
            }, status=status.HTTP_400_BAD_REQUEST)
