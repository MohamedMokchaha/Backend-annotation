from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentViewSet, AnnotationViewSet, export_annotations

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'annotations', AnnotationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('documents/export/<int:document_id>/', export_annotations, name='export_annotations'),
]

