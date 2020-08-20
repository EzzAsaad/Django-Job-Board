from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator

# Create your views here.


def Job_list(request):
    Job_list = Job.objects.all()
    paginator = Paginator(Job_list, 2)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj}
    return render(request, "job/jobs.html", context)


def Job_Details(request, id):
    Job_detail = Job.objects.get(id=id)
    #print(Job_Details)
    context = {"Job": Job_detail}
    return render(request, "job/job_details.html", context)
