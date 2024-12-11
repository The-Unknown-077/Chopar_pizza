from django.conf import settings
from django.conf.urls.static import static
from os import path

from django.contrib import admin

from apps.common.views import PizzaListCreateView,PizzaRetrieveUpdateDestroyView,OrderListCreateView,OrderRetrieveUpdateDestroyView,CustomerListCreateView,CustomerRetrieveUpdateDestroyView,DeliveryPersonListCreateView,DeliveryPersonRetrieveUpdateDestroyView,PaymentListCreateView,PaymentRetrieveUpdateDestroyView,CartRetrieveView,ProductListCreateView,CartItemAddView,CartItemDeleteView,PaymentCreateView

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pizzas/', PizzaListCreateView.as_view(), name='pizza-list-create'),
    path('pizzas/<int:pk>/', PizzaRetrieveUpdateDestroyView.as_view(), name='pizza-detail'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyView.as_view(), name='customer-detail'),
    path('delivery-persons/', DeliveryPersonListCreateView.as_view(), name='delivery-person-list-create'),
    path('delivery-persons/<int:pk>/', DeliveryPersonRetrieveUpdateDestroyView.as_view(), name='delivery-person-detail'),
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
      path('products/', ProductListCreateView.as_view(), name='product-list-create'),

    path('cart/', CartRetrieveView.as_view(), name='cart-retrieve'),
    path('cart/items/add/', CartItemAddView.as_view(), name='cart-item-add'),
    path('cart/items/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cart-item-delete'),

 
    path('payment/', PaymentCreateView.as_view(), name='payment-create'),
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
