from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/transcript/", include("transcript.urls", namespace="transcript")),
]
