from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from restapi import views

router = DefaultRouter()
router.register(r'apiusers', views.UserViewSet,)
urlpatterns = router.urls
router = DefaultRouter()
router.register(r'apiproducts', views.ProductViewSet)
urlpatterns += router.urls
router = DefaultRouter()
router.register(r'apiCompanys', views.CompanyViewSet)
urlpatterns += router.urls
