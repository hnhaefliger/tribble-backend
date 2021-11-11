from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .cortical import detect_language, detect_keywords


class LanguageViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'language'

    def create(self, request, *args, **kwargs):
        return Response(data=detect_language(request.data['text']), status=status.HTTP_200_OK)


class KeywordViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'language'

    def create(self, request, *args, **kwargs):
        return Response(data=detect_keywords(request.data['text']), status=status.HTTP_200_OK)
