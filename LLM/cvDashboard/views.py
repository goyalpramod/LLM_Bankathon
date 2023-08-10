from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
# from utils.LLM2_CV_score import func_


def cv_page(request):
    job_title = request.session.get('job_title', 'Default Job Title')  # You can provide a default value if it's not found.

    context = {
        'job_title': job_title
    }
    return render(request, 'cvDashboard/job.html', context)

# from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file=request.FILES['file']
        return (HttpResponse("NAME OF FILE:"+str(file)))
    else:
        form = UploadFileForm()
    return render(request, "job.html", {"form": form})

    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES["file"])
    #         return HttpResponseRedirect()
    #
