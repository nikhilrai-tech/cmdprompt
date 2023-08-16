from django.urls import path
from mainapp import views

urlpatterns = [
    # other URL patterns...
    path('execute/',views.execute_command, name='execute_command'),
    path('download/', views.download_output, name='download_output'),
]
