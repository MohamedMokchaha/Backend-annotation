from django.contrib import admin

from annotations.models import Document, Annotation

admin.site.register(Document)
admin.site.register(Annotation)