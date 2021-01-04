"""octave URL Configuration

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
from django.urls import path, include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
from rest_framework.documentation import include_docs_urls   # 追加
from rest_framework.schemas import get_schema_view # 追加

schema_view = get_schema_view(title='octave API') # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),   # 追加
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),   # 追加
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', schema_view), # 追加
    path('docs/', include_docs_urls(title='octave API')), # 追加
]
