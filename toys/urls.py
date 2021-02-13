from django.urls import path, re_path
from toys import views

app_name = 'toys'
urlpatterns = [
    # Base view da as_view chaqirilyapti path('', views.DashboardView.as_view(), name='dashboard'),
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('toys/', views.ToyListView.as_view(), name='toys'),
    path('toys/<int:pk>/', views.ToyDetailView.as_view(), name='toy_detail'),
    path('toys/create/', views.ToyCreateView.as_view(), name='toy-create')
    # re_path('toys/(?P<id>d+)/$', views.get_toy_detail, name='toy_detail')
]
