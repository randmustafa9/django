from django.shortcuts import render, redirect
from .models import Sponsor
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.admin import User
from django.views.decorators.csrf import requires_csrf_token
# Create your views here.



@requires_csrf_token
def signup_sponsor(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        fullName = request.POST.get("fullName")
        age = request.POST.get("age")
        birthDate = request.POST.get("birthDate")
        governorate = request.POST.get("governorate")
        job = request.POST.get("job")
        jobAddress = request.POST.get("jobAddress")
        phone = request.POST.get("phone")
        img = request.POST.get("img")
        monthlySalary = request.POST.get("monthlySalary")
        form1 = User.objects.create_user(username=username, password=password)
        form1.save()
        form2 = Sponsor(full_name=fullName, age=age, birth_date=birthDate, city=governorate, work=job, work_locations=jobAddress, number=phone, img=img, salary=monthlySalary)
        form2.save
        user = authenticate(request, username=username, password=password)
        login(request,user)
<<<<<<< HEAD
        return render(request,"bise.html")
    return render(request,signup_sponsor.html)
    def logins(request):
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return render(request,'bise.html',{'user':username})
            return render(request,'login.html')

    def logouts(request):
    if request.POST.get('logout'):
        logout(request)
            

=======
        return render(request,"sponsor_reg.html")
    return render(request, "sponsor_reg.html")
>>>>>>> c92bc89c6afada6bf9d2eb4b0e0c3fdb0351915e



 

 