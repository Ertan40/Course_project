from django.urls import path
from . import views


urlpatterns = (
    path('', views.index, name='index'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('catalogue/<str:name>', views.catalogue_view, name='catalogue'),
    path('catalogue/<str:cat_name>/<str:pro_name>', views.product_details, name='product details'),

)