from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.Job_list),
    path('<int:id>', views.Job_Details)
]