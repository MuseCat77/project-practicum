from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.urls import path
from polls.views import QuestionListView, VoteView
from cpus.views import ProductsListView


# API Root View (Отображает все маршруты в /)
class APIRootView(APIView):
    def get(self, request, format=None):
        return Response({
            "questions": reverse("question-list", request=request, format=format),
            "vote": request.build_absolute_uri("/api/questions/vote/{choice_id}/"),
            "cpus": reverse("cpus", request=request, format=format),
            "admin": "/admin/"
        })


urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),
    path('api/questions/', QuestionListView.as_view(), name='question-list'),
    path('api/questions/vote/<int:choice_id>/', VoteView.as_view(), name='vote'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # JSON: http://127.0.0.1:8000/api/cpus/
    # CSV: http://127.0.0.1:8000/api/cpus/?format=csv
    path('api/cpus/', ProductsListView.as_view(), name='cpus')
]
