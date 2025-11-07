from django.urls import path

from contactapp import views

urlpatterns=[
    path("contact/",views.contact,name="contact"),
    path("email/",views.email,name="email"),
    path("AI/",views.chatbot_view,name="AI"),
]