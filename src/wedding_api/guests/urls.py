from django.conf.urls import url
from django.conf.urls import include


from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('guests', views.GuestViewSet)

urlpatterns = [
  url(r'', include(router.urls))
]
