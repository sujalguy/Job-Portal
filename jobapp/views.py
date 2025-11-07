from django.shortcuts import render,redirect,get_object_or_404

from jobapp.forms import CreateItJobsForm,UpdateItJobsForm,CreateCIVILjobsform,CreateMechjobsform,UpdateMechJobs,UpdateCivilJobs
from django.contrib.auth.decorators import login_required
from jobapp.models import Itjobs
from jobapp.models import CIVILjobs
from jobapp.models import MECHjobs
from jobapp.forms import CustomUserCreationForm
from userapp.models import Applied_form
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request,'jobapp/home.html')

# ---------------------------------------------------------------------------------------------------------------------------------
@login_required
def welcome(request):
    if request.user.role == 'recruiter':
        return redirect('recruiter_dashboard')
    else:
        return redirect('user_dashbaord')
# ---------------------------------------------------------------------------------------------------------------------------------
@login_required
def recruiter_dashboard(request):
    return render(request, 'jobapp/recruiter_dashboard.html')
# --------------------------------------------------------------------------------------------------------------------------
@login_required
def manage_jobs(request):
    recruiter=request.user
    it_jobs = Itjobs.objects.filter(posted_by=recruiter)
    mech_jobs = MECHjobs.objects.filter(posted_by=recruiter)
    civil_jobs = CIVILjobs.objects.filter(posted_by=recruiter)

    context = {
        'it_jobs': it_jobs,
        'mech_jobs': mech_jobs,
        'civil_jobs': civil_jobs
    }
    return render(request, 'jobapp/manage_jobs.html', context)





# -----------------------------------------------------------------------------------------------------------------

def register(request):
    form=CustomUserCreationForm()
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            # send_mail(
            #     subject = "Welcome to JobPortal 🎉",
            #     message = f"Hi {user.username},\n\nThank you for registering on our Job Portal.\n\nNow you can login and start exploring jobs!\n\nRegards,\nJobPortal Team",
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list = [user.email],
            #     fail_silently=False,
            # )
            
            
            if user.role=="recruiter":
                return redirect ("login")
            elif user.role=="user":
                return redirect("login")
            else:
                return redirect("home")
            
        else:
            form = CustomUserCreationForm()  

    return render(request,'jobapp/register.html',{'form' : form})
# -------------------------------------------------------------------------------------------------------------------------------------------

@login_required
def create_IT_jobs(request):
    if request.method=='POST':
        form=CreateItJobsForm(request.POST)
        if form.is_valid():
            job=form.save(commit=False )
            job.posted_by=request.user
            job.save()
            return redirect('/recruiter-manage-jobs/')
            

    context={
        'form':CreateItJobsForm()

    }

    return render(request,'jobapp/create-it.html',context)



# -----------------------------------------------------------------------------------------------------------------------------------------


@login_required
def list_of_it_jobs(request):
    context={
        'data':Itjobs.objects.all()
    }
    return render(request,'jobapp/list_of_it_jobs.html',context)

# ---------------------------------------------------------------------------------------------------------------------------------

@login_required
def create_MECH_jobs(request):
    if request.method=='POST':
        form=CreateMechjobsform(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.posted_by=request.user
            job.save()
            return redirect('/recruiter-manage-jobs/')

    context={
        'form':CreateMechjobsform()
    }

    return render(request,'jobapp/create-mech.html',context)

# ----------------------------------------------------------------------------------------------------------------------------------------
@login_required
def list_mech_jobs(request):

    context={
        'data':MECHjobs.objects.all()
    }
    return render(request,'jobapp/list_of_mech_jobs.html',context)

# -------------------------------------------------------------------------------------------------

@login_required
def create_CIVIL_jobs(request):
    form = CreateCIVILjobsform()

    if request.method=='POST':
        form=CreateCIVILjobsform(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.posted_by=request.user
            job.save()
            return redirect("/recruiter-manage-jobs/")

    context={
        'form':CreateCIVILjobsform()
    }
    return render(request,'jobapp/create-civil.html',context)

# --------------------------------------------------------------------------------------------------------------------------------

@login_required
def list_of_civil_jobs(request):
    context={
        'data':CIVILjobs.objects.all()
    }
    return render(request,'jobapp/list_of_civil_jobs.html',context)


# -------------------------------------------------------------------------------------------------------------------------



@login_required
def update_it_jobs(request,id):
    obj=Itjobs.objects.get(pk=id,posted_by=request.user)

    if request.method=='POST':
        form= UpdateItJobsForm(request.POST , instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/recruiter-manage-jobs/")
        
    context = {
        'form': UpdateItJobsForm(instance=obj)
    }
    


    return render(request,'jobapp/update_it.html',context)
# ----------------------------------------------------------------------------------------------------------



@login_required
def update_mech_jobs(request,id):
    obj=MECHjobs.objects.get(pk=id,posted_by=request.user)

    if request.method=='POST':
        form=UpdateMechJobs(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/recruiter-manage-jobs/')
    context={
        'form':UpdateMechJobs(instance=obj)
    }

    return render(request,'jobapp/update-mech.html',context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------

@login_required

def update_civil_jobs(request,id):
    obj=CIVILjobs.objects.get(pk=id,posted_by=request.user)
    if request.method=='POST':
        form=UpdateCivilJobs(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/recruiter-manage-jobs/")
        
    context={
        'form':UpdateCivilJobs(instance=obj)
    }
    return render(request,'jobapp/update-civil.html',context)
# ------------------------------------------------------------------------------------------------------

@login_required
def delete_mech_jobs(request,id):
    obj=MECHjobs.objects.get(pk=id,posted_by=request.user)
    if request.method=='POST':
        obj.delete()
        return redirect('/recruiter-manage-jobs/') 
    return render(request,'jobapp/delete-mech.html',{"data":obj})



@login_required
def delete_civil_jobs(request,id):
    obj=CIVILjobs.objects.get(pk=id,posted_by=request.user)
    if request.method=='POST':
        obj.delete()
        return redirect('/recruiter-manage-jobs/')
    return render(request,'jobapp/delete-civil.html',{'data':obj})



@login_required
def delete_it_jobs(request , id):

    obj=Itjobs.objects.get(pk = id,posted_by=request.user)
    if request.method=='POST':
        obj.delete()
        return redirect('/recruiter-manage-jobs/')
    return render(request,'jobapp/delete-it.html',{'data':obj})


# --------------------------------------------------------------------------------------------------------------------------------

@login_required
def view_applications(request):
    user = request.user

    it_jobs = Itjobs.objects.filter(posted_by=user)
    mech_jobs = MECHjobs.objects.filter(posted_by=user)
    civil_jobs = CIVILjobs.objects.filter(posted_by=user)

    it_applications = Applied_form.objects.filter(
        job_type="it", job_id__in=it_jobs.values_list("id", flat=True)
    )
    mech_applications = Applied_form.objects.filter(
        job_type="mech", job_id__in=mech_jobs.values_list("id", flat=True)
    )
    civil_applications = Applied_form.objects.filter(
        job_type="civil", job_id__in=civil_jobs.values_list("id", flat=True)
    )

    applications = it_applications | mech_applications | civil_applications

    for app in applications:
        if app.job_type == "it":
            job = Itjobs.objects.filter(id=app.job_id).first()
        elif app.job_type == "mech":
            job = MECHjobs.objects.filter(id=app.job_id).first()
        elif app.job_type == "civil":
            job = CIVILjobs.objects.filter(id=app.job_id).first()
        else:
            job = None

        app.job_title = job.Job_title if job else "N/A"

    return render(request, "jobapp/view_applications.html", {"applications": applications})



# ---------------------------------------------------------------------------------------------------------------------------

def update_status(request, application_id, new_status):
    application = get_object_or_404(Applied_form, id=application_id)
    application.status = new_status
    application.save()
    return redirect("view_applications")


# -----------------------------------------------------------------------------------------------------------------------------------------

def About(request):
    return render(request,'jobapp/about.html')



