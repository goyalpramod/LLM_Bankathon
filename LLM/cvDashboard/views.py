from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from utils.LLM2_CV_score import func_, separator
from .models import CVs
from dotenv import load_dotenv, find_dotenv
import os
import smtplib
def cv_page(request):
    job_title = request.session.get('job_title', 'Default Job Title')  # You can provide a default value if it's not found.

    context = {
        'job_title': job_title
    }
    return render(request, 'cvDashboard/job.html', context)

# from somewhere import handle_uploaded_file
global CVmail, CVname
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file=request.FILES['file']
        cv1=CVs.objects.create(CV=file)
        pkkey=str(cv1)
        cvfile = CVs.objects.get(pk=int(pkkey[3:]))
        cvfile=cvfile.CV
        # with open(cv1.file.path, 'rb') as g:
        #     print(g)
        print(type(cvfile))
        data=func_(cvfile.path)
        separatedData=separator(data)
        print(separatedData)
        CVname=separatedData['name']
        CVmail=separatedData['email']
        CVscore=separatedData['score']
        context = {
            'form': form,
            'CVname': CVname,
            'CVscore': CVscore
        }
        return render(request, "cvDashboard/job.html", context)

        # return render(request, "job.html", {"form": form}, {"CVname" : CVname}, {"CVscore : CVscore"})
    else:
        form = UploadFileForm()
    return render(request, "cvDashboard/job.html", {"form": form})

    #     if form.is_valid():
    #         handle_uploaded_file(request.FILES["file"])
    #         return HttpResponseRedirect()
    #

def send_mail_to_candidate(request):

    load_dotenv(find_dotenv())
    email_pass = os.getenv("MAIL_PASSWORD")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('crusherscode0@gmail.com', email_pass)
    mailMessage=f"""
Dear {CVname},

We are pleased to inform you that your application for the position at Axis Bank has been shortlisted for further consideration. Your qualifications and experience have caught our attention, and we believe you could be a valuable addition to our team.

You will soon receive a link for a virtual interview. Please be on the lookout
During the interview, we will discuss your skills, experiences, and how they align with our organization's requirements. 

Please confirm your attendance at the interview by replying to this email or contacting us at crusherscode0@gmail.com. If the provided date and time are not suitable for you, kindly let us know, and we will try to arrange an alternative schedule.

We look forward to meeting you and learning more about your potential contribution to Axis Bank. Once again, congratulations on being shortlisted!

Best regards,
Hiring Manager
Axis Bank
"""
    server.sendmail('crusherscode0@gmail.com', CVmail , 'hey')
    print("mail sent")