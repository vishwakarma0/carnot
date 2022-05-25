from django.urls import include, path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('view', StudentInfoViewset)
router.register('students', StudentViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('samp/', samp),
    ]