from django.urls import path
from . import views
urlpatterns = [
    path('drill/', views.drill_get, name='drill'),
]