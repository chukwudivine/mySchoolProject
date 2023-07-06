from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('add-projects/', views.add_project, name='add_project'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('search/', views.projects),
    path("sorted/<int:department_id>/", views.sorted, name="sorted"),
    path('admin_panel/', views.admin, name='admin_page')
]
