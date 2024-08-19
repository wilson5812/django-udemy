from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.projects, name="projects"),
    path('projects/', views.projects, name="projects"),
    path('projects/<str:primary_key>/', views.project, name="project"),

    path('create/', views.create_project, name="create"),
    path('update/<str:primary_key>/', views.update_project, name="update"),
    path('delete/<str:primary_key>/', views.delete_project, name="delete"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)