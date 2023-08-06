from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # If you're using the default User model and username for authentication
        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)
            return redirect('dashboard_view')  # Or name of the view you want to redirect to after login.
        else:
            # Show an error or something if the credentials are wrong
            return HttpResponse("Wrong Credentials.")

    return render(request, 'accounts/login.html')
