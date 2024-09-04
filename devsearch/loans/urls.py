from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.loans, name="loans"),
    path('create/', views.create_loans, name="create_loans"),
]
