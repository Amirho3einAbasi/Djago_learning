from django.urls import path
from product.views import product_view_class,product_cls_detail_view,product_detail_view,ProductDetailSlugView

urlpatterns = [
    path('products', product_view_class.as_view(),name='product_list'),

    path('products-slug/<slug>', ProductDetailSlugView.as_view(),name='product_slug_view'),

    path('products-detail/<product_id>', product_detail_view),

    path('products-detail-cls/<pk>', product_cls_detail_view.as_view()),
    ]