from django.urls import path
from toys import views
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
]
