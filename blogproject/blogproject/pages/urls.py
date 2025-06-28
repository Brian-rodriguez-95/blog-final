from django.urls import path
from .views import (
    PageListView,
    PageDetailView,
    PageCreateView,
    PageUpdateView,
    PageDeleteView,
    AboutView,
)

urlpatterns = [
    path('', PageListView.as_view(), name='page_list'),
    path('<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    path('crear/', PageCreateView.as_view(), name='page_create'),
    path('<int:pk>/editar/', PageUpdateView.as_view(), name='page_update'),
    path('<int:pk>/borrar/', PageDeleteView.as_view(), name='page_delete'),
    path('about/', AboutView.as_view(), name='about'),
    path('', views.home, name='home'),


]