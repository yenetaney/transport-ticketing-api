from rest_framework.routers import DefaultRouter
from .views import TransportCompanyViewSet

router = DefaultRouter()
router.register(r'transport-companies', TransportCompanyViewSet, basename='transport-company')

urlpatterns = router.urls
