from django.conf.urls import url, include
from cndapp import views
from rest_framework.routers import DefaultRouter


# Create the router and register the viewsets with it
router = DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'preopassements', views.PreOpAssessmentViewSet)
router.register(r'opnotes', views.OpNoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^gender', views.PatientByGenderList.as_view(), name='gender'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

