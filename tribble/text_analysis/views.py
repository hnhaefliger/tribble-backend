from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .cortical import detect_language, detect_keywords
from .summary import generate_summary


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


class SummaryViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    lookup_url_kwarg = 'language'

    def create(self, request, *args, **kwargs):
        data = '<p>Keywords:    ' + '    '.join(detect_keywords(request.data['text'])) + '</p>'
        summary = generate_summary(request.data['text'])
        
        if summary != '':
            data += '<p>' + summary + '</p>'


        return Response(data=data, status=status.HTTP_200_OK)
