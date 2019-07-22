from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products/$', views.ProductList.as_view()),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.ProductDetail.as_view()),
]