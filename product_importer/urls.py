from django.contrib import admin
from django.urls import path
from .views import MyFileView, ProductsAPIView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('upload-csv/', csrf_exempt(MyFileView.as_view()), name='upload-csv'),
    path('products', ProductsAPIView.as_view()),
    path('products/<str:pk>', ProductsAPIView.as_view())
]
