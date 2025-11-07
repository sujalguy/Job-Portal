from django.urls import path

from jobapp import views

urlpatterns=[

    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path("welcome/",views.welcome ,name='welcome'),
   
    #recruiter urls 
    
    path('recruiter-dashboard/', views.recruiter_dashboard, name='recruiter_dashboard'),
    path('recruiter-manage-jobs/', views.manage_jobs,name='manage-jobs'),
   

    path("applications/", views.view_applications, name="view_applications"),
    path("applications/<int:application_id>/<str:new_status>/", views.update_status, name="update_status"),


    path('create-mech-jobs/',views.create_MECH_jobs ,name='create-mech-jobs'),
    path('list-mech-jobs/',views.list_mech_jobs ,name='list-mech-jobs'),
    path("update-mech-jobs/<int:id>/",views.update_mech_jobs,name='update-mech-jobs'),
    path("delete-mech-jobs/<int:id>/",views.delete_mech_jobs,name='delete-mech-jobs'),

    path('create-civil-jobs/',views.create_CIVIL_jobs, name='create-civil-jobs'),
    path('list-civil-jobs/',views.list_of_civil_jobs ,name='list-civil-jobs'),
    path('update-civil-jobs/<int:id>/',views.update_civil_jobs, name='update-civil-jobs'),
    path('delete-civil-jobs/<int:id>/',views.delete_civil_jobs ,name='delete-civil-jobs'),

    path('create-it-jobs/',views.create_IT_jobs, name='create-it-jobs'),
    path('list-it-jobs/',views.list_of_it_jobs ,name='list-it-jobs'),
    path('update-it/<int:id>/',views.update_it_jobs, name='update-it'),
    path('delete-it/<int:id>/',views.delete_it_jobs,name='delete-it'),


    path("about/",views.About,name="about")
    

]