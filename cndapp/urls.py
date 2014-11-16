from django.conf.urls import url, include
from cndapp import views
from rest_framework.routers import DefaultRouter


# Create a router and register the viewsets with it
router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'gender', views.GenderViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

