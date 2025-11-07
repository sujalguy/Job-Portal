from django.contrib import admin
from jobapp.models import Itjobs
from jobapp.models import MECHjobs
from jobapp.models import CIVILjobs
from jobapp.models import CustomUser

admin.site.register(Itjobs)
admin.site.register(MECHjobs)
admin.site.register(CIVILjobs)
admin.site.register(CustomUser)

