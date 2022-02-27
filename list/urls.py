from django.urls import path
from list import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'Home_app'
urlpatterns = [
    path('', views.home, name='Home'),
    path('auther/<int:auther_id>/', views.auther_view, name='Auther'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('details/<int:product_id>/',
         views.product_details, name='product_details'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart_page'),
    path('ad_to_cart/<int:cart_id>/', views.ad_to_cart, name='add_to_cart'),
    path('author/', views.author_view, name='author_list'),


]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
