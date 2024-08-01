# views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Document, Annotation
from .serializers import DocumentSerializer, AnnotationSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer

def export_annotations(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    annotations = document.annotations.all()

    export_data = {
        'document': document.text,
        'annotations': [
            {
                'start': annotation.start,
                'end': annotation.end,
                'label': annotation.label,
                'text': annotation.text
            }
            for annotation in annotations
        ]
    }

    return JsonResponse(export_data)
