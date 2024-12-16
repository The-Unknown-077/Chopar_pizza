from django.conf import settings
from django.conf.urls.static import static
from os import path
from django.contrib import admin
from django.urls import path
from apps.common import views
from .schema import swagger_urlpatterns

from apps.common.views import CartListCreateView,CartItemDeleteView, UserProfile


urlpatterns = [
    path("admin/", admin.site.urls),

    path('products/', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('product-prices/', views.ProductPriceListCreateAPIView.as_view(), name='product-price-list-create'),
    path('orders/', views.OrderListCreateAPIView.as_view(), name='order-list-create'),
    path('order-items/', views.OrderItemListCreateAPIView.as_view(), name='order-item-list-create'),
    path('contact-info/', views.ContactInfoListCreateAPIView.as_view(), name='contact-info-list-create'),
    path('users/', views.CustomUserListCreateAPIView.as_view(), name='custom-user-list-create'),
    path('user-locations/', views.UserLocationListCreateAPIView.as_view(), name='user-location-list-create'),
    path('cart/', CartListCreateView.as_view(), name='cart-list-create'),
    path('cart/item/<int:pk>/', CartItemDeleteView.as_view(), name='cart-item-delete'),
    path("request-code/", request_confirmation_code, name="request_code"),
    path("confirm-email/", confirm_email, name="confirm_email"),
    path('profile/', UserProfile.as_view())
]


urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
