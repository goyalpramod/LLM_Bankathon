from django.shortcuts import render

def cv_page(request):
    job_title = request.session.get('job_title', 'Default Job Title')  # You can provide a default value if it's not found.

    context = {
        'job_title': job_title
    }

    return render(request, 'cvDashboard/job.html', context)