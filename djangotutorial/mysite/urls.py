from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from polls.views import QuestionListView, VoteView
from cpus.views import ProductsListView

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/questions/', QuestionListView.as_view(), name='question-list'),
    path('api/questions/vote/<int:choice_id>/', VoteView.as_view(), name='vote'),
    path('', include(router.urls)),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/cpus/', ProductsListView.as_view(), name='cpus')
]
