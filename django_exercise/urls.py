"""django_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .view import home_page,next_page,login_paige,register_paige
from product.views import product_view_class,product_cls_detail_view,product_detail_view,ProductDetailSlugView
#static imports
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page),

    path('nextPage', next_page),

    path('login-site', login_paige),

    path('register', register_paige),

    path('',include('product.urls'))

]
if settings.DEBUG:
    urlpatterns = urlpatterns  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = urlpatterns  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)