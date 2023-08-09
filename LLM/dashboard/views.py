from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from utils.LLM import func_, divisor
import re
import json


@login_required
def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html')

def create_job(request):
    return render(request, 'dashboard/create.html')

@csrf_exempt
def process_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        job_title = data.get('job-title')
        job_description = data.get('job-description')
        request.session['job_title'] = job_title

        formatted_data = f"{job_title},{job_description}"
        values = func_(data=formatted_data)
        score,updatedJD, changes = divisor(values.content)
        updatedJD = re.sub(r'\n', '<br>', updatedJD)
        changes = re.sub(r'\n', '<br>', changes)

        # Process these using your LLM model and generate the results
        # For instance:
        # score = "8/10"
        # updatedJD = "Updated job description using LLM."
        print(values.content)
        print(score)
        return JsonResponse({"score": score, "updatedJD": updatedJD, "changes" : changes})
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405) 