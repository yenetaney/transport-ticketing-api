from rest_framework.routers import DefaultRouter
from .views import TransportCompanyViewSet, RouteViewSet, TripViewSet

router = DefaultRouter()
router.register(r'transport-companies', TransportCompanyViewSet, basename='transport-company')
router.register(r'routes', RouteViewSet, basename='route')
router.register(r'trip', TripViewSet, basename='trip')


urlpatterns = router.urls
