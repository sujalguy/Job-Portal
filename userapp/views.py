from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from jobapp.models import  Itjobs,MECHjobs,CIVILjobs
from userapp.forms import Studentjobs
from userapp.models import Applied_form
from django.contrib import messages
from userapp.models import UserLogin
from userapp.forms import EditProfile 

@login_required
def user_dashbaord(request):
    profile, created = UserLogin.objects.get_or_create(user=request.user)
    return render(request, "userapp/dashbaord.html", {"profile": profile})

@login_required
def  userlist_it_jobs(request):
    context={
        "data":Itjobs.objects.all()
        }
    return render(request,'userapp/list_it_jobs.html',context)

@login_required
def userlist_mech_jobs(request):
    context={
        "data":MECHjobs.objects.all()
        }
    return render(request,"userapp/list_MECH_jobs.html",context)

@login_required
def userlist_civil_jobs(request):
    context={
        "data":CIVILjobs.objects.all()
        }
    return render(request,"userapp/list_civil_jobs.html",context)

@login_required
def apply_job(request, job_type, job_id):
    if job_type == "it":
        job = get_object_or_404(Itjobs, id=job_id)
        job_type_value = "it"
    elif job_type == "mech":
        job = get_object_or_404(MECHjobs, id=job_id)
        job_type_value = "mech"
    elif job_type == "civil":
        job = get_object_or_404(CIVILjobs, id=job_id)
        job_type_value = "civil"
    else:
        messages.error(request, "Invalid job type")
        return redirect("user_dashbaord")
    
    if request.method == "POST":
        form = Studentjobs(request.POST, request.FILES)
        if form.is_valid():
            applied = form.save(commit=False)
            applied.user = request.user
            applied.job_type = job_type_value
            applied.job_id = job.id
            applied.save()
            messages.success(request, f"You have successfully applied for {job.Job_title}")
            return redirect("my_applications")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = Studentjobs()
    return render(request, "userapp/apply_job.html", {"form": form, "job": job})


@login_required
def my_applications(request):
    applications = Applied_form.objects.filter(user=request.user).order_by("-applied_at")
    return render(request, "userapp/my_applications.html", {"applications": applications})
    
@login_required
def profile_view(request):
    profile, created = UserLogin.objects.get_or_create(user=request.user)
    return render(request, "userapp/profile.html", {"profile": profile})

@login_required
def edit_profile(request):
    profile, created = UserLogin.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully ✅")
            return redirect("user_dashbaord")
    else:
        form = EditProfile(instance=profile)

    return render(request, "userapp/edit_profile.html", {"form": form})









