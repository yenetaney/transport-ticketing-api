from rest_framework.routers import DefaultRouter
from .views import TransportCompanyViewSet, RouteViewSet, TripViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'transport-companies', TransportCompanyViewSet, basename='transport-company')
router.register(r'routes', RouteViewSet, basename='route')
router.register(r'trip', TripViewSet, basename='trip')
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = router.urls
