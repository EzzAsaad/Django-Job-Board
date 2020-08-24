from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm
# Create your views here.


def Job_list(request):
    Job_list = Job.objects.all()
    paginator = Paginator(Job_list, 2)  # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"jobs": page_obj}
    return render(request, "job/jobs.html", context)


def Job_Details(request, slug):
    Job_detail = Job.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyForm(request.POST,request.FILES) #request.FILES is must be included or will no change in DB because file(s) with will not sent from form
        if form.is_valid():
            myform = form.save(commit = False)
            myform.job = Job_detail
            myform.save()
    else:
        form = ApplyForm()   
    context = {"Job": Job_detail,"form": form}
    return render(request, "job/job_details.html", context)
