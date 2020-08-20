from django.urls import path, include
from . import views
app_name = 'Job'

urlpatterns = [
    path('', views.Job_list),
    path('<int:id>', views.Job_Details, name="job_detail")
    #name to know name of url (in urls project called 'namespace')
]