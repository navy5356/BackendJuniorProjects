from django.contrib import admin
from django.urls import path
from revenue import views

urlpatterns = [
    path('revenue/', views.show, name="show"),
    path('admin/', admin.site.urls),
    path('collect/', views.collect, name="collect"),
]
