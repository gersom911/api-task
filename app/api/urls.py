from django.urls import path, include

from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import TaskViewSet


router: ExtendedSimpleRouter = ExtendedSimpleRouter()
router = routers.DefaultRouter()
router.register('task', TaskViewSet)
urlpatterns = [
    
        # YOUR PATTERNS
   
    #path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),  
    path('', include(router.urls))    

]