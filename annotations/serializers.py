# serializers.py
from rest_framework import serializers
from .models import Document, Annotation

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'start', 'end', 'label', 'text']

class DocumentSerializer(serializers.ModelSerializer):
    annotations = AnnotationSerializer(many=True, read_only=True)

    class Meta:
        model = Document
        fields = ['id', 'text', 'annotations']
