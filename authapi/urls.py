from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    
    path('api-auth/', ObtainAuthToken.as_view()),
    path('', include(router.urls)),
    path('getToken/', ObtainAuthToken.as_view())
    # include('rest_framework.urls', namespace='rest_framework'
]