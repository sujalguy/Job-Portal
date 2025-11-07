from django.urls import path
from django.contrib.auth.views import LogoutView
from userapp.views import *
from  django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("dashboard/",user_dashbaord ,name='user_dashbaord'),
    
    
    path("user-it-jobs/",userlist_it_jobs,name='user-it-jobs'),
    path("user-mech-jobs/",userlist_mech_jobs, name="user-mech-jobs"),
    path("user-civil-jobs/",userlist_civil_jobs, name="user-civil-jobs"),
    path("apply_job/<str:job_type>/<int:job_id>/",apply_job,name='apply_job'),
    path('my_applications/',my_applications,name='my_applications'),
    path("profile/",profile_view,name='profile_view'),
    path("edit_profile/",edit_profile, name="edit_profile"),
    path("logout/",LogoutView.as_view(next_page="login"),name="logout"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)