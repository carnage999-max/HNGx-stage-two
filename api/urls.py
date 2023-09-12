from . import views
from django.urls import path


urlpatterns = [
    path('', views.apiPostGet),
    path('<str:user_id>', views.apiPutDelete)
]

