from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm



def cv_page(request):
    job_title = request.session.get('job_title', 'Default Job Title')  # You can provide a default value if it's not found.

    context = {
        'job_title': job_title
    }
    return render(request, 'cvDashboard/job.html', context)

# from somewhere import handle_uploaded_file

# def upload_file(request):
    # if request.method == "POST":
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES["file"])
    #         return HttpResponseRedirect()
    # else:
    #     form = UploadFileForm()
    # return render(request, "upload.html", {"form": form})
    #
