from django.urls import path
from .views import inbox, send_message

urlpatterns = [
    path('inbox/', inbox, name='inbox'),
    path('enviar/', send_message, name='send_message'),
]