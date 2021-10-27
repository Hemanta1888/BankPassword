from django.urls import path
from . import views
app_name = 'quiz'
urlpatterns = [
    path('',views.home_page,name = 'homepage'),
    path('questions',views.view_form,name = 'questions'),
    path('submit/',views.submit_data,name = 'Submit')
    
]